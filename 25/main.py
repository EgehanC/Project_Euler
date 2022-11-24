fib_nums = [1, 1]


def new_fib_num():
    current_index = len(fib_nums) - 1
    new_fib = fib_nums[current_index] + fib_nums[current_index - 1]
    fib_nums.append(new_fib)


def main():
    while len(str(fib_nums[-1])) < 1000:
        new_fib_num()
    print(len(fib_nums))


main()
