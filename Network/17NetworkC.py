import socket

ip = "127.0.0.1"
open_ports = []


for port in range(1, 65536):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    if s.connect_ex((ip, port)) == 0:
        print(f"Port {port} is open")
        open_ports.append(port)
    s.close()

print("\nScan complete.")
if open_ports:
    print("Open ports:", open_ports)
else:
    print("No open ports found.")
