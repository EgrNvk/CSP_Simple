import socket

HOST = '127.0.0.1'
PORT = 4000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("Client connected")

msg = input("Enter math expression: ")
client.send(msg.encode())
print("Message sent")

data = client.recv(1024)
print("Server result:", data.decode())

client.close()
print("Client closed")