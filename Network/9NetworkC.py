import ipaddress

ip1 = input("enter first ip: ")
ip2 = input("enter first ip1: ")
mask = input("enter mask: ")

def same_subnet():
    global ip1, ip2, mask
    net1 = ipaddress.ip_network(f"{ip1}/{mask}", strict=False)
    net2 = ipaddress.ip_network(f"{ip2}/{mask}", strict=False)
    return net1.network_address == net2.network_address
print(same_subnet())