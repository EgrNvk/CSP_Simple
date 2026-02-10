import socket
import logging

logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

HOST = '127.0.0.1'
PORT = 4000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)


print("Server start")
logging.info("Server started")
conn, addr = server.accept()
print("Client connected by", addr)
logging.info(f"Client connected by {addr}")
while True:
    data = conn.recv(1024)
    msg = data.decode()
    print("Client msg:", msg)
    logging.info(f"Client msg: {msg}")

    if msg == "exit":
        logging.info("Client requested exit")
        break

    result = eval(msg)
    conn.send(str(result).encode())
    print("Client sent",result)
    logging.info(f"Client sent {result}")


conn.close()
server.close()
print("Server closed")
logging.info("Server closed")