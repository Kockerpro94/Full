Input = input("enter a String: ")
vowels = ["a", "e", "i", "o", "u"]

for char in Input:
    if char.lower() in vowels:
        print(f"The string contains the vowel: {char}")