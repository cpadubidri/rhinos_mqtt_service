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

# User built imports
from app.config import config
from app.parsers.topflytechcodec import T880xPlusEncoder

class MQTTClient:

    def __init__(self):
        self.client = mqtt.Client()
        self.message_event = Event()  # Event to signal when a message is received
        self.encoder = T880xPlusEncoder()

        # Set up callback for when a message is received
        self.client.on_message = self.on_message

    def connect(self):
        # Connect to the MQTT broker
        self.client.connect(config.MQTT_BROKER, config.MQTT_PORT)
        self.client.loop_start()

    def subscribe(self, topic):
        # Subscribe to the given topic
        self.client.subscribe(topic)

    def publish(self, topic, message):
        # Publish a message to the given topic
        self.client.publish(topic, message)

    def on_message(self, client, userdata, message):
        """
        Callback to handle incoming messages. Routes messages to the appropriate handler.
        """
        print(f"Message received on topic '{message.topic}': {message.payload.decode('utf-8')}")
        self.message_event.set()  # Signal that a message was received

        # Forward the message to the TopicHandler
        if "_S" in message.topic:  # Check if it's a login topic
            response = self.topic_handler.handle_login_message(message.topic, message.payload)
            print(f"Generated response: {response}")

            # Publish the response to the corresponding response topic
            response_topic = message.topic.replace("_S", "_R")  # Replace _S with _R
            self.publish(response_topic, response)


if __name__ == "__main__":
    # Initialize MQTT client
    mqtt_client = MQTTClient()

    # Connect to the MQTT broker
    mqtt_client.connect()

    # Subscribe to all topics
    mqtt_client.subscribe("#")

    print("Subscribed to '#' (all topics). Waiting for a message...")

    try:
        # Wait for a message to be received
        while True:
            mqtt_client.message_event.wait()  # Wait until a message is received
            mqtt_client.message_event.clear()  # Reset the event for the next message
            print("Waiting for the next message...")
    except KeyboardInterrupt:
        print("Exiting program...")


