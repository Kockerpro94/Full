import socket
import threading

PORT = 6060
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(ADDR)

print(f"[STARTING] UDP server is starting on {SERVER}:{PORT}")

clients = set()  # Track client addresses

def handle_message(data, addr):
    message = data.decode(FORMAT)
    print(f"[{addr}] {message}")
    
    if message == DISCONNECT_MESSAGE:
        print(f"[DISCONNECTED] {addr} left")
        clients.discard(addr)
    else:
        clients.add(addr)
        # Example: echo back to sender
        s.sendto(f"Server received: {message}".encode(FORMAT), addr)

def start():
    print(f"[LISTENING] UDP server is ready on {SERVER}:{PORT}")
    while True:
        data, addr = s.recvfrom(1024)  # Receive up to 1024 bytes
        threading.Thread(target=handle_message, args=(data, addr)).start()

start()
