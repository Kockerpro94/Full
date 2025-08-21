import socket
from datetime import datetime

def tcp_port_scanner(target_host, start_port, end_port):
    print(f"Scanning ports on {target_host} from {start_port} to {end_port}...")
    print("-" * 50)
    start_time = datetime.now()

    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1) 

            result = sock.connect_ex((target_host, port))

            if result == 0:
                print(f"Port {port} is open")
            sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved.")
    except socket.error:
        print("Could not connect to server.")
    except KeyboardInterrupt:
        print("\nExiting program.")

    end_time = datetime.now()
    total_time = end_time - start_time
    print("-" * 50)
    print(f"Scanning finished in: {total_time}")

if __name__ == "__main__":
    target = input("Enter the target IP address or hostname: ")
    try:
        start_p = int(input("Enter the starting port number: "))
        end_p = int(input("Enter the ending port number: "))
        if start_p > end_p or start_p < 1 or end_p > 65535:
            print("Invalid port range. Please enter valid port numbers (1-65535).")
        else:
            tcp_port_scanner(target, start_p, end_p)
    except ValueError:
        print("Invalid port number. Please enter integers.")