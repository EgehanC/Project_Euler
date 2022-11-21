import time

start = time.time()


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


def sum_divisors(n):
    sum = 0
    divs = divisors(n)
    if divs:
        divs.pop()
    for divisor in divs:
        sum += divisor
    return sum


def main():
    div_sum_list = {}
    for i in range(0, 10001):
        div_sum = sum_divisors(i)
        div_sum_list[i] = div_sum
    sum = 0
    for j in div_sum_list:
        if div_sum_list[j] in div_sum_list:
            if j == div_sum_list[div_sum_list[j]]:
                sum += j
                sum += div_sum_list[j]
    print(sum)

main()
end = time.time()
print(f"Time: {end - start}")
