import string

def check_password_strength(password):
    if len(password) < 8:
        return "Your password is too short. Make it at least 8 characters."
    
    if not any(char.isdigit() for char in password):
        return "Add at least one number to make it stronger."
    
    if not any(char in string.punctuation for char in password):
        return "Throw in a special character (!, @, #, etc.) for extra security."
    
    return "Nice! Your password looks strong."


user_password = input("Type your password: ")
print(check_password_strength(user_password))
