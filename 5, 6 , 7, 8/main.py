# ### Problem 5
# n = 2
# i = 1
# while i < 21:
#     if n % i == 0:
#         i += 1
#     else:
#         i = 1
#         n += 1
# print(n)

# ### Problem 6
# def dif():
#     sum = 0
#     sumofsquares = 0
#     for i in range(1, 101):
#         sumofsquares += i ** 2
#         sum += i
#     squareofsum = sum ** 2
#     print(f"Sum = {sum}, Square of the sum = {squareofsum}, Sum of the squares = {sumofsquares}")
#     print(squareofsum - sumofsquares)
#
#
# dif()

# ### Problem 7
# def isPrimeNumber(n):
#     dividers_of_x = [1, n]
#     if n % 2 == 0:
#         while n % 2 == 0:
#             n /= 2
#         dividers_of_x.append(2)
#     for i in range(3, round(n ** 1 / 2)):
#         if n % i == 0:
#             dividers_of_x.append(i)
#
#     if len(dividers_of_x) > 2:
#         return False
#     elif len(dividers_of_x) <= 2:
#         return True
#
#
# prime_numbers = [2]
# i = 3
# while len(prime_numbers) < 10001:
#     if isPrimeNumber(i):
#         prime_numbers.append(i)
#     i += 2
# print(prime_numbers[-1])

# ### Problem 8
# def product_adj(n):
#     number_list = list(n)
#     i = 0
#     biggest = 0
#     while i + 12 < len(number_list):
#         mult = 1
#         for j in range(i, i+13):
#             mult *= int(number_list[j])
#         if mult > biggest:
#             biggest = mult
#         i += 1
#     print(biggest)
#
# number = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
# product_adj(number)
