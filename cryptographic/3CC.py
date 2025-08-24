import hashlib

Result = hashlib.md5(b"Hello, World!").hexdigest()
print(Result)