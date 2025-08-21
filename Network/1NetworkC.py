while True:
    input_Ter = input("type to see this is ip IPv4 or IPv6: ")
    input_Ter_number = len(input_Ter)
    if '.' in input_Ter and input_Ter_number > 10:
        print("This is an IPv4 address.")
        break
    if '192.168.' in input_Ter:
        print("This is a private IPv4 address.")
        break   
    if input_Ter_number < 11 and ':' in input_Ter:
        print("This is an IPv6 address.")
        break
    if input_Ter == 'exit':
        print("Exiting the program.")
        break
    else:
        print("Error: Invalid input. Please try again.")