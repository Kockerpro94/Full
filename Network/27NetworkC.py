import random
import time

def generate_seq():
    return random.randint(1000, 9999)

def tcp_handshake_simulation():
    client_seq = generate_seq()
    server_seq = generate_seq()

    print("Client: sending SYN")
    print(f"Client Seq={client_seq}")
    time.sleep(1)

    print("Server: received SYN, sending SYN-ACK")
    print(f"Server Seq={server_seq}, ACK={client_seq + 1}")
    time.sleep(1)

    print("Client: received SYN-ACK, sending ACK")
    print(f"Client ACK={server_seq + 1}")
    time.sleep(1)

    print("\nTCP connection established!")

if __name__ == "__main__":
    tcp_handshake_simulation()
