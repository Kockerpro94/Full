import os

version = os.popen('ver').read().strip()
print(version)
