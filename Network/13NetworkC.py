import socket

ip = input("Enter target IP address: ").strip()
open_ports = []

print(f"\nScanning {ip} for open ports 1–1000...\n")

for port in range(1, 1001):
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
