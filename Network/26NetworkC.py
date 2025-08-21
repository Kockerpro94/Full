import socket
from datetime import datetime

host = '0.0.0.0'
port = 9999
log_file = "tcp_connections.log"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen(5)

print(f"Listening for incoming TCP connections on port {port}...")

try:
    while True:
        conn, addr = server.accept()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - Connection from {addr[0]}:{addr[1]}"
        print(log_entry)
        with open(log_file, "a") as f:
            f.write(log_entry + "\n")
        conn.close()
except KeyboardInterrupt:
    print("\nStopped.")
    server.close()
