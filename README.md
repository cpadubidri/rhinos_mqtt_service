# rhinos_mqtt_service




### Block diagram

    +-------------------------+          +------------------------+         +-----------------------+
    | PioneerX 101 Hub        |          | Ubuntu Server          |         | ThingsBoard Dashboard |
    | (Bluetooth Sensor Data) |   MQTT   | (MQTT Broker + Python) |   MQTT  | (Data Visualization)  |
    |                         +--------->+                        +-------->+                       |
    +-------------------------+          +------------------------+         +-----------------------+



### Folder structure

    mqtt_iot_service/
    ├── README.md                 # Project documentation
    ├── requirements.txt          # Python dependencies
    ├── tests/                    # Unit and integration tests
    │   ├── test_codecs.py         # Tests for TopflytechCodec
    │   ├── test_mqtt_client.py    # Tests for MQTT communication
    │   ├── test_data_processor.py # Tests for data processing
    │   └── test_integration.py    # End-to-end tests
    ├── app/                      # Main application directory
    │   ├── __init__.py           # Makes `app/` a package
    │   ├── config/               # Configuration files
    │   │   ├── config.py         # Centralized configuration logic
    │   │   ├── constants.py      # Application constants
    │   ├── core/                 # Core functionality
    │   │   ├── __init__.py
    │   │   ├── mqtt_client.py    # MQTT client setup and communication
    │   │   ├── data_processor.py # Processes decoded data
    │   │   ├── logger.py         # Logging utility
    │   │   ├── db_handler.py     # Database interaction logic (future)
    │   │   ├── logic_engine.py   # Custom processing logic (future)
    │   │   └── forwarder.py      # Forwards data to custom dashboard (future)
    │   ├── parsers/              # Parsing and decoding logic
    │   │   ├── __init__.py
    │   │   └── TopflytechCodec.py # Decoder for PioneerX 101
    │   ├── thingsboard/          # ThingsBoard-specific integration
    │   │   ├── __init__.py
    │   │   ├── thingsboard_api.py # ThingsBoard MQTT API client
    │   │   └── tb_data_mapper.py  # Maps data to ThingsBoard format
    └── main.py                   # Entry point for the application


    
    app/
    ├── core/
    │   ├── mqtt_client.py         # Manages MQTT connectivity and subscriptions
    │   ├── message_handler.py     # Handles decoding and processing logic
    │   ├── response_handler.py    # Handles responding to login and other messages
    │   └── forwarder.py           # Sends telemetry data to ThingsBoard or other destinations

