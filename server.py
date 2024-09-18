import socket
import threading

HEADER = 64
PORT = 5050
HOSTNAME = socket.gethostname()
SERVER = socket.gethostbyname(HOSTNAME)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"New Connection {addr} Connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"{addr} {msg}")
            conn.send("MESSAGE RECEIVED".encode(FORMAT))

def start():
    server.listen()
    print(f"Server IP {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active Connections {threading.activeCount() - 1}")


print("Starting Server")
start()


