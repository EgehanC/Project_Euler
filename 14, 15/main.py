### Problem 14
def longest_collatz_sequence(n):
    # sequence = f"{n}"
    chain_len = 0
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
        # sequence += f"-->{n}"
        chain_len += 1
    # print(sequence)
    return chain_len


def main14():
    max_len = 0
    for i in range(2, 10 ** 6):
        current_len = longest_collatz_sequence(i)
        if current_len > max_len:
            max_len = current_len
            number = i
    print(number)

# main14()

### Problem 15



def main15():



main15()
