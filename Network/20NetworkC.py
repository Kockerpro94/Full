import socket

ports_services = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    79: "Finger",
    80: "HTTP",
    88: "Kerberos",
    110: "POP3",
    111: "RPC",
    119: "NNTP",
    123: "NTP",
    135: "MS RPC",
    137: "NetBIOS Name",
    138: "NetBIOS Datagram",
    139: "NetBIOS Session",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    500: "ISAKMP / IKE",
    514: "Syslog",
    515: "LPD Printer",
    520: "RIP",
    587: "SMTP Submission",
    631: "IPP Printing",
    993: "IMAPS",
    995: "POP3S"
}

ip = input("Enter target IP address: ").strip()
open_ports = []

print(f"\nScanning {ip} for high-risk reserved ports...\n")

for port, service in ports_services.items():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    if s.connect_ex((ip, port)) == 0:
        print(f"Port {port} OPEN - {service}")
        open_ports.append((port, service))
    s.close()

print("\nScan complete.")
if open_ports:
    print("\nSummary of open high-risk ports:")
    for p, s in open_ports:
        print(f"{p} - {s}")
else:
    print("No risky ports found.")
