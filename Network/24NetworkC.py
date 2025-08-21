import socket, time

def tcp_rtt(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    start = time.time()
    s.connect((host, port))
    end = time.time()
    s.close()
    return (end - start) * 1000

print(tcp_rtt("google.com", 80))
