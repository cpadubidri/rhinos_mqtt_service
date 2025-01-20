# import pika
# import json
# import random
# import time

# # RabbitMQ Configuration
# RABBITMQ_HOST = 'localhost'
# QUEUE_NAME = 'imei_56454125'

# # Function to simulate sensor data
# # def generate_sensor_data():
# #     return {
# #         "imei": f"{random.randint(1000000000000000, 9999999999999999)}",  # Random IMEI
# #         "temperature": round(random.uniform(20.0, 30.0), 2),             # Random temperature
# #         "humidity": round(random.uniform(40.0, 60.0), 2),               # Random humidity
# #         "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")                 # Current timestamp
# #     }


# def generate_sensor_data():
#     return {
#         "accessToken": "hcho7i9lg39094iasyde",  # Replace with the actual token
#         "data": {
#             "imei": "56454125",  # Fixed IMEI for testing
#             "temperature": round(random.uniform(20.0, 30.0), 2),  # Random temperature
#             "humidity": round(random.uniform(40.0, 60.0), 2),     # Random humidity
#             "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")       # Current timestamp
#         }
#     }


# # RabbitMQ Connection
# connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
# channel = connection.channel()

# # Declare the queue (if it doesn't already exist)
# # channel.queue_declare(queue=QUEUE_NAME)
# # Declare the queue (if it doesn't already exist)
# channel.queue_declare(queue=QUEUE_NAME, durable=True)


# print("Simulating sensor data... Press Ctrl+C to stop.")

# try:
#     while True:
#         # Generate simulated data
#         data = generate_sensor_data()
        
#         # Publish data to RabbitMQ
#         channel.basic_publish(
#             exchange='',  # Default exchange
#             routing_key=QUEUE_NAME,  # Send to the test queue
#             body=json.dumps(data)
#         )
        
#         print(f"Sent to RabbitMQ: {data}")
        
#         # Wait 2 seconds before sending the next message
#         time.sleep(10)

# except KeyboardInterrupt:
#     print("\nSimulation stopped.")
# finally:
#     connection.close()



import pika
import json
import random
import time

# RabbitMQ Configuration
RABBITMQ_HOST = '192.168.178.41'  # Replace with your RabbitMQ server IP
RABBITMQ_PORT = 5672
RABBITMQ_USERNAME = 'rhinos_thingsboard'  # Replace with RabbitMQ username
RABBITMQ_PASSWORD = 'rhinos@123'  # Replace with RabbitMQ password
# RABBITMQ_QUEUE = 'thingsboard'
RABBITMQ_QUEUE = 'tb_rule_engine.queue'

# Connect to RabbitMQ
credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT, credentials=credentials))
channel = connection.channel()

# Declare the queue (durable for reliability)
channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)

# Function to generate simulated sensor data

def generate_sensor_data():
    return {
        "deviceName": "RD0001-3F_KCN_NFRG-PX101-TSTH1B",  # Match the device name in ThingsBoard
        "telemetry": {  # Use 'telemetry' to directly provide telemetry data
            "temperature": round(random.uniform(10.0, 50.0), 2),
            "humidity": round(random.uniform(40.0, 60.0), 2),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
    }



print("Simulating sensor data... Press Ctrl+C to stop.")

try:
    while True:
        # Generate sensor data
        sensor_data = generate_sensor_data()
        
        # Publish data to RabbitMQ
        channel.basic_publish(
            exchange='',  # Default exchange
            routing_key=RABBITMQ_QUEUE,  # Queue name
            body=json.dumps(sensor_data),
            properties=pika.BasicProperties(delivery_mode=2)  # Make message persistent
        )
        
        print(f"Sent to RabbitMQ: {sensor_data}")
        
        # Wait 2 seconds before sending the next message
        time.sleep(2)

except KeyboardInterrupt:
    print("\nSimulation stopped.")
finally:
    # Close the RabbitMQ connection
    connection.close()



# 25euktvw1vz3bjtbtghe