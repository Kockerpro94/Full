#maked by kockerpro94
# second code in network
a = input("enter ip for get binary Code: ")
b = len(a)

if '.' in a:
    print("Binary representation of the first octet (if it's a valid number):")
    try:
        octets = a.split('.')
        if octets:
            print(bin(int(octets[0])))
    except ValueError:
        print("Invalid IP format for binary conversion.")