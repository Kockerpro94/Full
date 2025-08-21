import ipaddress

def calculate_network_broadcast(ip_address, subnet_mask):
    """
    Calculates the network address and broadcast address given an IP address and subnet mask.

    Args:
        ip_address (str): The IP address in string format (e.g., "192.168.1.10").
        subnet_mask (str): The subnet mask in string format (e.g., "255.255.255.0").

    Returns:
        tuple: A tuple containing the network address (str) and broadcast address (str).
               Returns (None, None) if an invalid IP or subnet mask is provided.
    """
    try:
        # Create an IPv4Interface object from the IP address and subnet mask
        # This automatically calculates network and broadcast addresses
        network_interface = ipaddress.IPv4Interface(f"{ip_address}/{subnet_mask}")

        # Extract the network address
        network_address = str(network_interface.network.network_address)

        # Extract the broadcast address
        broadcast_address = str(network_interface.network.broadcast_address)

        return network_address, broadcast_address
    except ipaddress.AddressValueError as e:
        print(f"Error: Invalid IP address or subnet mask provided. {e}")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None

ip = input("Enter IP Address: ")
mask = input("Enter Subnet Mask: ")
network, broadcast = calculate_network_broadcast(ip, mask)

if network and broadcast:
    print(f"IP Address: {ip}")
    print(f"Subnet Mask: {mask}")
    print(f"Network Address: {network}")
    print(f"Broadcast Address: {broadcast}")
