import socket
import struct
import os

def get_host_ip():
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = socket.gethostbyname(socket.gethostname())
    finally:
 # Ensure the socket is closed even if an exception occurs
        if s:
            s.close()
    return ip

def main():
    if os.name == 'nt':
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        host_ip = get_host_ip()
        print(f"Binding to interface: {host_ip}")
        sniffer.bind((host_ip, 0))
        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    else:
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

    print("Packet sniffer started. Press Ctrl+C to stop.")

    try:
        while True:
            raw_buffer, addr = sniffer.recvfrom(65535)

            ip_header = raw_buffer[0:20]
            iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

            version_ihl = iph[0]
            ihl = version_ihl & 0xF
            ip_header_length = ihl * 4
            protocol = iph[6]
            s_addr = socket.inet_ntoa(iph[8])
            d_addr = socket.inet_ntoa(iph[9])

            print(f'\n[+] IP Packet: {s_addr} -> {d_addr} | Protocol: {protocol}')

            if protocol == 6:
                tcp_header = raw_buffer[ip_header_length:ip_header_length+20]
                tcph = struct.unpack('!HHLLBBHHH', tcp_header)
                
                source_port = tcph[0]
                dest_port = tcph[1]
                
                print(f'    [TCP] {s_addr}:{source_port} -> {d_addr}:{dest_port}')

            elif protocol == 17:
                udp_header = raw_buffer[ip_header_length:ip_header_length+8]
                udph = struct.unpack('!HHHH', udp_header)

                source_port = udph[0]
                dest_port = udph[1]
                
                print(f'    [UDP] {s_addr}:{source_port} -> {d_addr}:{dest_port}')

    except KeyboardInterrupt:
        print("\nStopping sniffer.")
    finally:
        if os.name == 'nt':
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
            sniffer.close()

if __name__ == '__main__':
    main()