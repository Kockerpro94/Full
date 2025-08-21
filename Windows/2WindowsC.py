import os

computer_name = os.environ.get("COMPUTERNAME")
user_name = os.getlogin()

print(f"Computer Name: {computer_name}")
print(f"Logged-in User: {user_name}")
