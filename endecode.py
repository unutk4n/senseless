import base64

message = "Python is fun"
message_bytes = message.encode('utf-8')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('utf-8')
print(base64_message)
