#maked by kocekrpro94
# this code is easy
def Main():
    input_Ter = input("type to see this private ip or no: ")
    if '192.168.' in input_Ter:
        print("this is private ip")
    if '.' in input_Ter:
        print("this is public ip")

Main()