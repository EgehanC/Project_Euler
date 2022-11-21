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


def sum_divisors(a, b):
    div_sum_list = {}
    for i in range(a, b):
        sum = 0
        divs = divisors(i)
        divs.pop()
        for divisor in divs:
            sum += divisor
        div_sum_list[i] = sum

    return div_sum_list


def main():
    div_sum_list = sum_divisors(1, 10001)
    amicable_nums = []
    for j in div_sum_list:
        if div_sum_list[j] in div_sum_list and j != div_sum_list[j] and div_sum_list[div_sum_list[j]] == j:
            amicable_nums.append(j)
    # Calculating sum
    sum = 0
    for num in amicable_nums:
        sum += num
    # Printing results
    print(f"Amicable numbers: {amicable_nums}")
    print(f"Sum: {sum}")


main()
end = time.time()
print(f"Time: {end - start}")