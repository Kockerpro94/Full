import socket

server_ip = input("Enter server IP or hostname: ")
port = 23
timeout = 5

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(timeout)

try:
    sock.connect((server_ip, port))
    print(f"Telnet is allowed on {server_ip}:{port}")
except (socket.timeout, socket.error):
    print(f"Telnet is NOT allowed on {server_ip}:{port}")
finally:
    sock.close()
