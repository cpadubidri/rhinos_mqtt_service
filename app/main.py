from app.core.mqtt_client import MQTTClient





if __name__ == "__main__":
    # Initialize the MQTT client
    mqtt_client = MQTTClient()

    # Connect to the broker
    mqtt_client.connect()

    # Keep the script running
    try:
        import time
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        mqtt_client.disconnect()