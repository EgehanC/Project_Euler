def recurring_cycle(n):

    remainders = []
    for i in n:
        if i not in remainders:
            remainders.append(i)

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



