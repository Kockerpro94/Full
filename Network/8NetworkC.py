def get_ipv4_class(ip_address):
    try:
        first_octet = int(ip_address.split('.')[0])
    except (ValueError, IndexError):
        return "Invalid IP Address"

    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    elif 240 <= first_octet <= 254:
        return "Class E (Experimental)"
    else:
        return "Invalid IP Address"
