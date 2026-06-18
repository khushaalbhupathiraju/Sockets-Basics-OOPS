import socket

'''SERVER = socket.gethostbyname(socket.gethostname())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 5050
FORMAT = 'utf-8'
HEADER = 64
ADDR = (SERVER, PORT)
DISCONNECT_MSG = "DISCONNECTED"
client.connect(ADDR)
server_details = client.getpeername()
print(f"[SUCCESSFUL] Connected to {server_details}")

def Send_server(message):
    msg = message.encode(FORMAT)
    msg_len = len(msg)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(msg)
    
Send_server("Hello World")
Send_server(DISCONNECT_MSG)
d_message = client.recv(1024).decode(FORMAT)
print(d_message)'''


class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.PORT = 5050
        self.FORMAT = 'utf-8'
        self.HEADER = 64
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER, self.PORT)
        self.DISCONNECT_MSG = "DISCONNECTED"

        self.client.connect(self.ADDR)
        self.server_details = self.client.getpeername()
        print(f"[SUCCESSFUL] Connected to {self.server_details}")
        self.Send_server("Hello World")
        self.Send_server(self.DISCONNECT_MSG)
        self.d_message = self.client.recv(1024).decode(self.FORMAT)
        print(self.d_message)

    def Send_server(self, message):
        msg = message.encode(self.FORMAT)
        msg_len = len(msg)
        send_len = str(msg_len).encode(self.FORMAT)
        send_len += b' ' * (self.HEADER - len(send_len))
        self.client.send(send_len)
        self.client.send(msg)

client = Client()
        
