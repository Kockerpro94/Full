import ipaddress

def get_ips_in_subnet(subnet_cidr):
    try:
        network = ipaddress.ip_network(subnet_cidr)
        ip_list = [str(ip) for ip in network.hosts()]
        return ip_list
    except ValueError as e:
        print(f"Error: Invalid subnet CIDR '{subnet_cidr}'. {e}")
        return []


subnet = input("Enter a subnet CIDR (e.g., '192.168.1.0/24'): ")
all_ips = get_ips_in_subnet(subnet)

if all_ips:
    print(f"All possible IP addresses in {subnet}:")
    for ip in all_ips:
        print(ip)