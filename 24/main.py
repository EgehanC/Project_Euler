from math import factorial


def nth_lexicographic_perm(char_list, n):
    total_perm = factorial(len(char_list))
    nth_perm = ""
    perms_by_number = total_perm / len(char_list)
    chars_left = len(char_list)
    while len(nth_perm) < len(char_list):
        k = int(n / perms_by_number)
        nth_perm += char_list[k-1]
        char_list.remove(char_list[k-1])
        chars_left -= 1
        perms_by_number /= chars_left
        n /= chars_left

    nth_perm += char_list[0]
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
