string = input("type string to reverse it: ")

def Reverse_words():
    global string
    reversed_string = string[::-1]
    print(reversed_string)


Reverse_words()