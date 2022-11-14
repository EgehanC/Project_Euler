# Problem 9
from math import sqrt

def pythagorean_triplet(n):
    for b in range(n):
        for a in range(1, b):
            c = sqrt(a**2 + b**2)

            if c % 1 == 0 and a + b + c == 1000:
                print(a, b, c)
                print(f"The product is {a*b*c}")
                break

pythagorean_triplet(1000)