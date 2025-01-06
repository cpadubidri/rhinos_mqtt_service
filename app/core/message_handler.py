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



    def login_message(self, topic, payload):
        payload_hex = bytes.fromhex(payload.decode())       
        login_data = self.decoder.decode(payload_hex)
        message = login_data[0]
        print(message)

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


if __name__=="__main__":
    msg = MessageHandler()
    data = b'252501001700BC08672840627807560000241115100611'

    decoded = msg.login_message("X", data)
