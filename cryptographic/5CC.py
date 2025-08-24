import hashlib

Input = input("Enter a password to hash: ")


Result = hashlib.sha256(Input.encode()).hexdigest()
print(Result)