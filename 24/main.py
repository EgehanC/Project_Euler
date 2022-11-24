from math import factorial, ceil
import time


def nth_lexicographic_perm(char_list, n):
    # initiating variables
    total_perm = factorial(len(char_list))
    total_chars = len(char_list)
    nth_perm = ""
    perms_by_number = total_perm / total_chars
    chars_left = total_chars

    # creating the wanted permutation
    while len(nth_perm) < total_chars:

        index = ceil(n / perms_by_number)

        # to prevent index reversing
        if index == 0:
            k = 1
        # adding new character
        nth_perm += char_list[index - 1]
        # removing the added character
        char_list.remove(char_list[index - 1])

        if n > perms_by_number:
            n %= perms_by_number
        chars_left -= 1
        # to prevent division with 0
        if chars_left != 0:
            perms_by_number /= chars_left

    return nth_perm


def main():
    # asking the list and the permutation wanted
    char_list = input("Enter characters: 1, 2, ...\n").split(", ")
    n = int(input("nth permutation, n = "))

    # to prevent out of range inputs
    while factorial(len(char_list)) < n or n < 1:
        print("Please enter a existing permutation")
        n = int(input("nth permutation, n = "))

    start = time.time()
    char_list.sort()
    print(nth_lexicographic_perm(char_list, n))
    end = time.time()
    print(f"Time: {round(end - start, 6)}")


main()


