import socket
import random
import struct

def build_dns_query(domain):
    tid = random.randint(0, 65535)
    flags = 0x0100
    qdcount = 1
    ancount = 0
    nscount = 0
    arcount = 0

    header = struct.pack(">HHHHHH", tid, flags, qdcount, ancount, nscount, arcount)

    query = b""
    for part in domain.split("."):
        query += struct.pack("B", len(part)) + part.encode()
    query += b"\x00"
    qtype = 1
    qclass = 1
    query += struct.pack(">HH", qtype, qclass)

    return header + query, tid

def parse_dns_response(data, tid):
    resp_tid = struct.unpack(">H", data[:2])[0]
    if resp_tid != tid:
        print("Transaction ID mismatch")
        return
    print("Received DNS response:")
    print(data.hex())

if __name__ == "__main__":
    server = ("8.8.8.8", 53)
    domain = input("Enter domain to query: ")

    packet, tid = build_dns_query(domain)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5)
    sock.sendto(packet, server)

    try:
        data, _ = sock.recvfrom(512)
        parse_dns_response(data, tid)
    except socket.timeout:
        print("No response from server")
    finally:
        sock.close()
