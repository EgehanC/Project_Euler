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


# Initializing the lists
abundant_list = []
abundant_list_sums = []


def main():
    start = time.time()
    for i in range(12, 28123):
        isAbundant(i)
    for num1 in abundant_list:
        for num2 in abundant_list:
            sum = num1 + num2
            if sum < 28123:
                abundant_list_sums.append(sum)

    sum = 0
    for i in abundant_list_sums:
        sum += i

    print(f"{28123*28122/2-sum}")

    sum = 0

    end = time.time()
    print(f"Time: {round(end-start, 6)}")


main()
