import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 59000))
server.listen()

print("server is listening...")

client, addr = server.accept()
print(f"Connected by {addr}")

# First, receive metadata separately to avoid conflicts
metadata = client.recv(1024).decode('utf-8').strip()
file_name, file_size = metadata.split('|')
file_size = int(file_size)

print(f"File name: {file_name}")
print(f"File size: {file_size}")

# Prepare to receive the file data
file = open(file_name, "wb")

received_size = 0
while received_size < file_size:
    data = client.recv(1024)
    file.write(data)
    received_size += len(data)

file.close()
client.close()
server.close()
print(f"File {file_name} received successfully")
