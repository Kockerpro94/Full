def is_privileged_port(port):
    return 0 <= port <= 1023

port = int(input("Enter a port number: "))

if is_privileged_port(port):
    print(f"Port {port} is in the privileged range.")
else:
    print(f"Port {port} is not in the privileged range.")
