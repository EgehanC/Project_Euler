### Problem 9
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

### Problem 10


def isPrimeNumber(n):
    dividers_of_x = [1, n]
    for i in range(3, round(n ** (1 / 2)+1), 2):
        if n % i == 0:
            while n % i == 0:
                n /= i
            dividers_of_x.append(i)
        if n == 1:
            break

    if len(dividers_of_x) > 2:
        return False
    else:
        return True


def sum_of_primes():
    sum = 2
    for i in range(3, 2000000, 2):
        if isPrimeNumber(i):
            sum += i
    print(sum)


sum_of_primes()
print("test")
