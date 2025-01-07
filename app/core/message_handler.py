# Libraries
from colorama import Fore, Style, init
from tabulate import tabulate

# User built imports
from app.parsers.topflytechcodec import T880xPlusEncoder
from app.parsers.topflytechcodec import Decoder, MessageEncryptType, SignInMessage
from app.utils.utils import get_timestamp



# Initialize colorama
init(autoreset=True)

class MessageHandler:
    def __init__(self):
        self.encoder = T880xPlusEncoder(messageEncryptType=None,aesKey=None)
        self.decoder = Decoder(MessageEncryptType.NONE, None)
    
    # def handle_message(self, topic, payload):
    #     if "_S" in topic:  # Login message
    #         self.login_message(topic, payload)



    def handle_message(self, topic, payload):
        payload_hex = bytes.fromhex(payload.decode())

        print(payload[:6].decode('utf-8'))
        if payload[:6].decode('utf-8')=="252501": #Login Message
            return self.login_message(topic, payload)
            
        elif payload[:6].decode('utf-8')=="252502": #Heartbeat Message
            # print(payload)
            return None, None
        
        elif payload[:6].decode('utf-8')=="252510": #BLE Message 
            # print(payload)
            return None, None
        
        elif payload[:6].decode('utf-8')=="252513": #Position Message
            # print(payload)
            return None, None
        
        elif payload[:6].decode('utf-8')=="252514": #Alarm Message 
            # print(payload)
            return None, None
        
        else:
            print(payload)
            return None, None
    
    def login_message(self,topic, payload_hex): #login Message
        login_data = self.decoder.decode(payload_hex)
        message = login_data[0]

        print(f"{Fore.CYAN}[{get_timestamp()}] {Fore.GREEN}[INFO]{Fore.RESET} Login message received for {Fore.YELLOW}IMEI No:{message.imei}{Style.RESET_ALL}")
        data = [
                [f"{Fore.BLUE}IMEI{Style.RESET_ALL}", f"{Fore.YELLOW}{message.imei}{Style.RESET_ALL}"],
                [f"{Fore.BLUE}Serial Number{Style.RESET_ALL}", f"{Fore.YELLOW}{message.serialNo}{Style.RESET_ALL}"],
                [f"{Fore.BLUE}Software Version{Style.RESET_ALL}", f"{Fore.YELLOW}{message.software}{Style.RESET_ALL}"],
                [f"{Fore.BLUE}Hardware Version{Style.RESET_ALL}", f"{Fore.YELLOW}{message.hardware}{Style.RESET_ALL}"],
                [f"{Fore.BLUE}Needs Response{Style.RESET_ALL}", f"{Fore.YELLOW}{message.isNeedResp}{Style.RESET_ALL}"],
            ]

        print(
                f"{Fore.CYAN}[{get_timestamp()}] {Fore.GREEN}[LOGIN INFO]{Fore.RESET} "
                f"Device details"
            )
        # Print the table
        print(tabulate(data, tablefmt="psql"))

        if message.isNeedResp:
            login_response = self.encoder.getSignInMsgReply(message.imei, True, message.serialNo)
            response_topic = topic.replace("_S", "_R")  # Replace '_S' with '_R'

            # Return the response and topic to MQTTClient
            return response_topic, login_response
        return None, None

    def heartbeat_message(self,topic, payload_hex): #Heartbeat Message
        pass

    def ble_message(self,topic, payload_hex): #BLE Message 
        pass

    def position_message(self,topic, payload_hex): #Position Message
        pass

    def alaram_message(self,topic, payload_hex): #Alarm Message
        pass



if __name__=="__main__":
    msg = MessageHandler()
    data = b'252501001700BC08672840627807560000241115100611'

    decoded = msg.login_message("X", data)
