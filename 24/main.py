from math import factorial
import time

start = time.time()


def nth_lexicographic_perm(char_list, n):
    # initiating variables
    total_perm = factorial(len(char_list))
    total_chars = len(char_list)
    nth_perm = ""
    perms_by_number = total_perm / total_chars
    chars_left = total_chars

    # creating the wanted permutation
    while len(nth_perm) < total_chars:
        
        k = round(n / perms_by_number)

        # to prevent index reversing
        if k == -1:
            k = 0
        # adding new character
        nth_perm += char_list[k - 1]
        # removing the added item
        char_list.remove(char_list[k - 1])

        chars_left -= 1
        # to prevent division with 0
        if chars_left != 0:
            n /= chars_left
            perms_by_number /= chars_left

    print(nth_perm)


def main():
    char_list = input("Enter characters: 1, 2, ...\n").split(", ")
    n = int(input("nth permutation, n = "))
    while factorial(len(char_list)) > n > factorial(len(char_list)):
        print("Please enter a existing permutation")
        n = int(input("nth permutation, n = "))
    char_list.sort()

    nth_lexicographic_perm(char_list, n)


main()
end = time.time()
print(f"Time: {end - start}")
