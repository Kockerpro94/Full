import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"Result: {hostname}  {ip_address}")
