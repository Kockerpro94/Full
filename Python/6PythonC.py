# Even or Odd Checker

num = input("Enter a number: ")

# Validate input
if not num.strip().lstrip('-').isdigit():
    print("That's not a valid integer!")
else:
    num = int(num)
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

