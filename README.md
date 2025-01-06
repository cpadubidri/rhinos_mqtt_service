# rhinos_mqtt_service


## Overview

This project is a smart system designed to connect and manage multiple **PioneerX 101 Hubs**, which collect data from Bluetooth sensors like temperature and humidity. The data is processed on an Ubuntu server and visualized on a user-friendly dashboard powered by **ThingsBoard**.

The system facilitates seamless communication between hardware devices, the server, and the dashboard, making it easy to monitor environmental data in real-time.

---

## System Workflow

The system operates in three main stages:

### 1. Data Collection
- **PioneerX 101 Hubs** collect data from connected Bluetooth sensors (e.g., temperature and humidity).
- The hub sends this data to the Ubuntu server using a communication protocol called **MQTT**.

### 2. Data Processing
- The **Ubuntu server** acts as the brain of the system. It:
  - Receives data from the hubs.
  - Decodes and validates the data.
  - Prepares the data for visualization.
- The server ensures that all hubs are logged in and authenticated before sending their data.

### 3. Data Visualization
- The processed data is sent to the **ThingsBoard Dashboard**.
- Users can view real-time sensor data in an intuitive, graphical interface.

---

## System Design

Here’s a simplified diagram of how the system works:

    +-------------------------+          +------------------------+         +-----------------------+
    | PioneerX 101 Hub        |          | Ubuntu Server          |         | ThingsBoard Dashboard |
    | (Bluetooth Sensor Data) |   MQTT   | (MQTT Broker + Python) |   MQTT  | (Data Visualization)  |
    |                         +--------->+                        +-------->+                       |
    +-------------------------+          +------------------------+         +-----------------------+



---

## Features

### 1. Device Management
- Automatically authenticates each PioneerX 101 Hub.
- Tracks device status and activity.

### 2. Real-Time Data
- Collects and processes data in real-time.
- Displays temperature, humidity, and other sensor readings instantly.

### 3. Centralized Dashboard
- Provides a single dashboard to monitor all devices and their data.
- Allows non-technical users to view graphs, charts, and reports.

### 4. Scalability
- Can handle multiple hubs and sensors, making it suitable for large-scale deployments.



### Directory structure:

    Rhinos_mqtt_service.git/
    ├── README.md
    ├── app/
    │   ├── __init__.py
    │   ├── main.py
    │   ├── config/
    │   │   ├── __init__.py
    │   │   └── config.py
    │   ├── core/
    │   │   ├── __init__.py
    │   │   ├── data_processor.py
    │   │   ├── message_handler.py
    │   │   ├── mqtt_client.py
    │   │   └── mqtt_client_.py
    │   ├── parsers/
    │   │   ├── __init__.py
    │   │   └── topflytechcodec.py
    │   └── utils/
    │       ├── __init__.py
    │       └── utils.py
    └── test/
        ├── clear_publish.py
        └── test_decoder.py


