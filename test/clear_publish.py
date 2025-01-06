import paho.mqtt.client as mqtt

# Connect to the broker
client = mqtt.Client()
client.connect("0.0.0.0", 4444)

# Publish a null (empty) retained message
client.publish("867284062780756_R", payload=None, retain=True)

# Disconnect
client.disconnect()