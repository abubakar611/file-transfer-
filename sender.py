import os
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 59000))

file_path = "image.jpg"
file_name = "received_image.jpg"
file_size = os.path.getsize(file_path)

# Send metadata
metadata = f"{file_name}|{file_size}"
client.sendall(metadata.encode('utf-8'))

# Send file data
with open(file_path, "rb") as file:
    while True:
        data = file.read(1024)
        if not data:
            break
        client.sendall(data)

client.close()
print(f"File {file_path} sent successfully")
