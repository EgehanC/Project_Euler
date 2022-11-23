import time


# finds divisors of n using quadrativ sieve
def divisor_gen(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            yield i
            if i != n / i:
                divisors.insert(0, n / i)
    for div in divisors:
        yield div


def divisors(n):
    return [d for d in divisor_gen(n)]


# Categorizes the number given a number
def isAbundant(n):
    divs = divisors(n)
    # removing the last divisor (itself)
    divs.pop(-1)

    # Summing its divisors
    sum_of_divs = 0
    for divisor in divs:
        sum_of_divs += divisor
    if sum_of_divs > n:
        abundant_list.append(n)


# Initializing the list
abundant_list = []

sums_of_abundants = [0]*28124
def main():
    start = time.time()
    for i in range(1, 28124):
        isAbundant(i)
    for num1 in range(0, len(abundant_list)):
        for num2 in range(num1, len(abundant_list)):
            sum_of_2 = abundant_list[num1] + abundant_list[num2]
            if sum_of_2 <= 28123:
                if sums_of_abundants[sum_of_2] == 0:
                    sums_of_abundants[sum_of_2] = sum_of_2

    total = 0
    for i in range(0, len(sums_of_abundants)):
        if sums_of_abundants[i] == 0:
            total += i

    end = time.time()
    print(f"Total: {total}")
    print(f"Time: {round(end - start, 6)}")


main()
