# Problem 12

# returnes n'th triangle number
def triangle_num(n):
    tri_num = (n*(n+1))/2
    return tri_num
    

# finds divisors of n using quadrativ sieve
def divisor_gen(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            yield i
            if i != n / i:
                divisors.insert(0, n / i)
    for div in divisors:
        yield div


def divisors(n):
    return [d for d in divisor_gen(n)]


num_divs = 0
i = 1
while num_divs < 500:
    i += 1
    num = triangle_num(i)
    divs = divisors(num)
    num_divs = len(divs)

print(divs)
print()
print(num)