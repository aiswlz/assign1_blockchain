from random import randint, getrandbits
from hash import hash

def generate_keys(bits=512):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    def mod_inverse(a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    def is_prime(n, k=5):
        if n <= 1 or n % 2 == 0:
            return False
        if n <= 3:
            return True

        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2

        for _ in range(k):
            a = randint(2, n - 1)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue

            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False

        return True

    def generate_prime(bits):
        while True:
            p = getrandbits(bits)
            if is_prime(p):
                return p

    p, q = generate_prime(bits // 2), generate_prime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Common choice for e
    while gcd(e, phi) != 1:
        e = randint(2, phi)
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def encrypt(message, public_key):
    e, n = public_key
    message_int = int.from_bytes(message.encode(), 'big')
    return pow(message_int, e, n)

def decrypt(ciphertext, private_key):
    d, n = private_key
    message_int = pow(ciphertext, d, n)






