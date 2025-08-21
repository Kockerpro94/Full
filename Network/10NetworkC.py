
common_ports = {
    20: "FTP (Data Transfer)",
    21: "FTP (Command Control)",
    22: "SSH (Secure Shell)",
    23: "Telnet",
    25: "SMTP (Email Sending)",
    53: "DNS (Domain Name System)",
    67: "DHCP (Server)",
    68: "DHCP (Client)",
    69: "TFTP (Trivial File Transfer)",
    80: "HTTP (Web Traffic)",
    110: "POP3 (Email Retrieval)",
    123: "NTP (Time Sync)",
    143: "IMAP (Email Retrieval)",
    161: "SNMP (Monitoring)",
    443: "HTTPS (Secure Web Traffic)",
    3389: "RDP (Remote Desktop Protocol)"
}


print("Common Ports and Services:\n")
for port, service in common_ports.items():
    print(f"Port {port:<5} → {service}")
