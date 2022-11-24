def recurring_cycle(n):
    print(n)
    n = str(n)[2:]
    print(n)
    cycle = []
    for i in n:
        if i not in cycle:
            cycle.append(i)

    return len(cycle)


def main():
    max_cycle = 0
    num = 0
    for d in range(2, 1001):
        print(f"Current d: {d}")
        current_cycle = recurring_cycle(round(1/d, 30))
        if current_cycle > max_cycle:
            max_cycle = current_cycle
            num = d
    print(num)


main()



