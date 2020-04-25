from Crypto.Util.number import *
from Crypto import Random
import Crypto


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


bits = 60
msg = "HELLO"

p = int(input("Дай p "))
q = int(input("Дай q "))

n = p * q
PHI = (p - 1) * (q - 1)

e = int(input("Дай e "))
d = modinv(e, PHI)

m = bytes_to_long(msg.encode('utf-8'))

print(d)

c = pow(m, e, n)
res = pow(c, d, n)

print("Message=%s\np=%s\nq=%s\nN=%s\ncipher=%s\ndecipher=%s" %
      (msg, p, q, n, c, (long_to_bytes(res))))

