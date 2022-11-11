# ### Problem 1
# def sum_multiples(n):
#     sum = 0
#     for i in range(3, n):
#         if i % 15 == 0:
#             sum += i
#         elif i % 5 == 0:
#             sum += i
#         elif i % 3 == 0:
#             sum += i
#     print(sum)
#
# sum_multiples(1000)

# ### Problem 2
# fib_nums = [1, 2]
#
#
# def sum_even_fibs():
#     n = int(input("Calculate fibonacci numbers until n. \nn = "))
#     sum = 2
#     index = 0
#     while fib_nums[len(fib_nums) - 1] < n:
#         new_fib = fib_nums[index] + fib_nums[index + 1]
#         fib_nums.append(new_fib)
#         if new_fib % 2 == 0:
#             sum += new_fib
#         index += 1
#     if fib_nums[len(fib_nums) - 1] > n:
#         if fib_nums[len(fib_nums) - 1] % 2 == 0:
#             sum -= fib_nums[len(fib_nums) - 1]
#         fib_nums.remove(fib_nums[len(fib_nums) - 1])
#     print(sum)
#     print(fib_nums)
#
#
# sum_even_fibs()

# ### Problem 3
# import math
#
#
# def maxPrimeFactors(n):
#     maxPrime = -1
#     while n % 2 == 0:
#         maxPrime = 2
#         n /= 2
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         while n % i == 0:
#             maxPrime = i
#             n /= i
#     if n > 2:
#         maxPrime = n
#     return int(maxPrime)
#
#
# n = 600851475143
# print(maxPrimeFactors(n))

