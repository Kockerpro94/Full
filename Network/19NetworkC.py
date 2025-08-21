import socket
import sys

def udp_scan(target_host, start_port, end_port, timeout=1):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(timeout)
        try:
            sock.sendto(b"test", (target_host, port))
            data, addr = sock.recvfrom(1024)
            open_ports.append(port)
        except socket.timeout:
            pass
        except socket.error as e:
            pass
        finally:
            sock.close()
    return open_ports

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python udp_scanner.py <target_host> <start_port> <end_port>")
        sys.exit(1)

    target_host = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    print(f"Scanning UDP ports on {target_host} from {start_port} to {end_port}...")
    found_ports = udp_scan(target_host, start_port, end_port)

    if found_ports:
        print("Open UDP ports found:")
        for p in found_ports:
            print(f"- {p}")
    else:
        print("No open UDP ports found in the specified range.")