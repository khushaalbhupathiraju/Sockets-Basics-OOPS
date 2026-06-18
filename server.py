import socket
import threading

'''def client_handle(connection, address):
    print(f'Connected to {address}')

    connected = True
    while connected:
        msg_len = connection.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            message = connection.recv(msg_len).decode(FORMAT)
            if message == DISCONNECT_MSG:
                connected = False
                connection.send("Disconnected!!".encode())
               
            print(f'[MESSAGE] Client{(address)} Message: {message}')

    connection.close()

def start():
    print("[SERVER INITIALISATION] Server Is Live!")
    server.listen()
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=client_handle, args=(connection, address))
        thread.start()
        print(f"[ACTIVE THREADS]: {threading.active_count() - 1}")'''

class Server:

    def __init__(self):
        # Configuration
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.PORT = 5050
        self.HEADER = 64
        self.ADDRESS = (self.SERVER, self.PORT)
        self.FORMAT = "utf-8"
        self.DISCONNECT_MSG = "DISCONNECTED"

        # Create socket
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind socket to address
        self.server.bind(self.ADDRESS)

    def client_handle(self, connection, address):

        print(f"[CONNECTED] {address}")

        connected = True

        while connected:

            # Receive message length
            msg_length = connection.recv(self.HEADER).decode(self.FORMAT)

            if msg_length:

                msg_length = int(msg_length)

                # Receive actual message
                message = connection.recv(msg_length).decode(self.FORMAT)

                print(f"[MESSAGE] Client {address}: {message}")

                if message == self.DISCONNECT_MSG:
                    connected = False
                    connection.send("Disconnected!".encode(self.FORMAT))

        connection.close()

        print(f"[DISCONNECTED] {address}")

    def start(self):

        print("[SERVER INITIALIZATION] Server is Live!")

        self.server.listen()

        while True:

            # Wait for client
            connection, address = self.server.accept()

            # Create thread
            thread = threading.Thread(
                target=self.client_handle,
                args=(connection, address)
            )

            thread.start()

            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


if __name__ == "__main__":

    server = Server()
    server.start()