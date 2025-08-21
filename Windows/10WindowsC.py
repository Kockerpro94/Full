import os


var_name = os.getcwd()  # the environment variable to check
if var_name in os.environ:
    print(f"{var_name} exists")
else:
    print(f"{var_name} does not exist")
