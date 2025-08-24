import hashlib 

Input = input("Enter text to hash: ")
Result = hashlib.sha1(Input.encode()).hexdigest()
print(Result)