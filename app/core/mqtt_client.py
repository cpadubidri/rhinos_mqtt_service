"""
Module Name: example_module.py
Author: Chirag Padubidri
Version: 1.0.0
Created: 2025-01-03
Description: This module is responsible for managing mqtt communication
like connect to broker, subscribe to topics, and publish messages.
"""

# Libraries
import paho.mqtt.client as mqtt
from threading import Event
from colorama import Fore, Style, init



# User built imports
from app.config import config
from app.parsers.topflytechcodec import T880xPlusEncoder
from app.core.message_handler import MessageHandler
from app.utils.utils import get_timestamp

# Initialize colorama
init(autoreset=True)

class MQTTClient:

    def __init__(self):
        self.client = mqtt.Client()
        self.message_event = Event()  # Event to signal when a message is received
        self.message_handler = MessageHandler()

        # Set up callback methods
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

        #debugging
        self.return_code = {0: "Connection successful.",
                            1: "Connection refused - incorrect protocol version.",
                            2: "Connection refused - invalid client identifier.",
                            3: "Connection refused - server unavailable.",
                            4: "Connection refused - bad username or password.",
                            5: "Connection refused - not authorized."
                            }
    
    def connect(self):
        self.client.connect(config.MQTT_BROKER, config.MQTT_PORT)
        self.client.loop_start()

    
    def on_connect(self, client, userdata, flags, rc, topic='#'):
        print(  f"{Fore.CYAN}[{get_timestamp()}] {Fore.GREEN}[INFO]{Fore.RESET} "
                f"Broker Connection: {Fore.YELLOW}Code={rc}{Fore.RESET}, "
                f"{Fore.YELLOW}Message={self.return_code[rc]}{Fore.RESET}"
            )
        # Subscribe to all device topics
        # self.client.subscribe(topic)
        self.client.subscribe("#")#("#", 0), options=mqtt.SubscribeOptions(noLocal=True))

    def on_message(self, client, userdata, msg):
        print(  f"{Fore.CYAN}[{get_timestamp()}] {Fore.GREEN}[INFO]{Fore.RESET} "
                f"Message received on topic {Fore.YELLOW}{msg.topic}{Style.RESET_ALL}"
            )

        # self.message_handler.handle_message(msg.topic, msg.payload)

        if "_S" in msg.topic:
            # Login message
            response_topic, response = self.message_handler.login_message(msg.topic, msg.payload)
            if response_topic and response:
                self.publish(response_topic, response)
        # elif "_data" in msg.topic:
        #     # Data message (e.g., telemetry or sensor data)
        #     self.message_handler.login_message(msg.topic, msg.payload)
        elif "_R" in msg.topic:
            pass
        else:
            print(msg.topic, '>>>>>', msg.payload)

    def on_disconnect(self, client, userdata, rc):
        print("Disconnected from MQTT broker")
        if rc != 0:
            print("Unexpected disconnection. Attempting to reconnect...")
            self.connect()
    
    def publish(self, topic, payload):
        """
        Publish a message to the MQTT broker.
        """
        self.client.publish(topic, payload.hex())
        print(
                f"{Fore.CYAN}[{get_timestamp()}] {Fore.GREEN}[LOGIN INFO]{Fore.RESET} "
                f"Published message to topic={topic}, response={payload.hex()}"
            )

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        print("Disconnected from MQTT broker")