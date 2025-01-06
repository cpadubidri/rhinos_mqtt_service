import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.parsers.topflytechcodec import Decoder, MessageEncryptType, SignInMessage, T880xPlusEncoder

# Initialize the decoder
decoder = Decoder(MessageEncryptType.NONE, None)
encoder = T880xPlusEncoder(messageEncryptType=None,aesKey=None)

# Raw login data from the hub
raw_data = b'\x25\x25\x01\x00\x17\x00\x04\x08\x67\x28\x40\x62\x78\x07\x56\x00\x00\x24\x11\x15\x10\x06\x11'


# Decode the data
decoded_messages = decoder.decode(raw_data)

print(type(decoded_messages[0]))

# Process the decoded messages
for message in decoded_messages:
    print(f"IMEI: {message.imei}")
    print(f"Serial Number: {message.serialNo}")
    print(f" MCU Version: {message.software}")
    print(f"Hardware Version: {message.hardware}")
    print(f"Needs Response: {message.isNeedResp}")

    # Generate a login response if required
    if message.isNeedResp:
        response = encoder.getSignInMsgReply(message.imei, True, message.serialNo)

        print(response)

