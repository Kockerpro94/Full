import socket

INPUT = input("Enter the message to send to the server: ")
PORT = 6060  # use a high port to avoid permission errors
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.12"
ADDR = (SERVER, PORT)

# Create UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send(msg):
    client.sendto(msg.encode(FORMAT), ADDR)  # Send message to server
    try:
        client.settimeout(2)  # Wait max 2 seconds for reply
        data, server_addr = client.recvfrom(1024)
        print(f"Server replied: {data.decode(FORMAT)}")
    except socket.timeout:
        print("No response from server.")

send(INPUT)

# Optionally send disconnect message
send(DISCONNECT_MESSAGE)

client.close()
