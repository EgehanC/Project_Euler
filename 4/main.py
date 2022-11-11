# ### Problem 4
def isPalindrome(word):
    rev_word = word[::-1]
    if rev_word == word:
        return True
    else:
        return False


def find_max():
    num1 = 1000
    num2 = 1000
    max = 0
    for i in range(0, 100):
        num1 -= 1
        for j in range(0, 100):
            num2 -= 1
            new_int = num1 * num2
            new_str = str(new_int)
            if isPalindrome(new_str) and new_int > max:
                max = new_int
        num2 += 100
    print(max)


find_max()
