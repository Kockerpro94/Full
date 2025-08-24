import math

def factor_n(n):
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    raise ValueError("Failed to factor n")

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = extended_gcd(b % a, a)
    return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError("No modular inverse exists")
    return x % m

n = 3233
e = 17
ciphertext = 855

p, q = factor_n(n)
phi = (p - 1) * (q - 1)
d = modinv(e, phi)

plaintext = pow(ciphertext, d, n)
print(f"p = {p}, q = {q}")
print(f"d = {d}")
print(f"Decrypted message: {plaintext}")
