### Problem 14
from time import time


def longest_collatz_sequence(n):
    # sequence = f"{n}"
    chain_len = 0
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
        # sequence += f"-->{n}"
        chain_len += 1
    # print(sequence)
    return chain_len


def main14():
    start = time()
    max_len = 0
    for i in range(2, 10 ** 6):
        current_len = longest_collatz_sequence(i)
        if current_len > max_len:
            max_len = current_len
            number = i
    end = time()
    print(f"{number} has the largest sequence")
    print(f"Time: {end - start}")


# main14()


### Problem 15
from math import factorial


def routes_btw_ab(x, y):
    return int(factorial(x + y) / (factorial(x) * factorial(y)))


def main15():
    x = int(input("What is the 1. dimension: "))
    y = int(input("What is the 2. dimension: "))
    route_count = routes_btw_ab(x, y)
    print(f"Number of routes from A to B is {route_count}")


# main15()


### Problem 16
def sum_digits(n):
    n = str(n)
    sum = 0
    for i in n:
        i = int(i)
        sum += i
    return sum


def main16():
    n = int(input("n = "))
    n = n ** int(input("power = "))
    print(sum_digits(n))

# main16()
