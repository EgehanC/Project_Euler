def recurring_cycle(n):
    remainders = []
    current_remainder = 1 % n
    while current_remainder not in remainders:
        remainders.append(current_remainder)
        current_remainder = (current_remainder * 10) % n

    print(remainders)
    return len(remainders)


def main():
    max_cycle = 0
    num = 0
    for d in range(2, 1001):
        print(f"Current d: {d}")
        current_cycle = recurring_cycle(d)
        if current_cycle > max_cycle:
            max_cycle = current_cycle
            num = d
    print(num)


main()
