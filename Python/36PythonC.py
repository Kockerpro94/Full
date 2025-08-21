import random

def random_mac():
    parts = []
    for _ in range(6):
        num = random.randint(0, 255) 
        parts.append(f"{num:02x}")
    return ":".join(parts)

for i in range(5):
    print(random_mac())
