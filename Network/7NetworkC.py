import ipaddress

ipv6_expanded = input("Enter an IPv6 address in expanded form: ")
ipv6_obj = ipaddress.IPv6Address(ipv6_expanded)
ipv6_compressed = ipv6_obj.compressed
print(f"Compressed form: {ipv6_compressed}")