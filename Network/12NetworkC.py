Input = input("enter to know the port valid or no: ")

def Main(port):
    return isinstance(port, int) and 0 <= port <= 65535

print(Main(Input))