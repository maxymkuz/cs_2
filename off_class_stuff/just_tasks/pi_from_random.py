from random import random

points_in = 0
n = 1000000

for i in range(n):
    if (random()**2 + random()**2) ** 0.5 < 1:
        points_in += 1

print(4 * points_in / n)
