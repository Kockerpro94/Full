import socket

target_ip = input("Enter the IP to check: ").strip()
port = int(input("Enter the port number: "))

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.settimeout(0.5)
tcp_result = tcp_sock.connect_ex((target_ip, port))
tcp_sock.close()

udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_sock.settimeout(0.5)
try:
    udp_sock.sendto(b"Hello", (target_ip, port))
    udp_sock.recvfrom(1024)
    udp_result = True
except socket.timeout:
    udp_result = False
except ConnectionRefusedError:
    udp_result = True
finally:
    udp_sock.close()

if tcp_result == 0:
    print(f"Port {port} is open and uses TCP.")
elif udp_result:
    print(f"Port {port} is open and likely uses UDP.")
else:
    print(f"Port {port} is closed or not responding.")
