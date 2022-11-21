### Problem 18
import time

start = time.time()


def main():
    with open('18.txt') as f:
        # All the numbers in the file
        number = f.read()

    # splitting the number into a list
    number = number.strip().split('\n')

    # converting each and every list of strings to int
    for i in range(1, len(number)):
        number[i] = number[i].strip().split(' ')
        number[i] = [int(x) for x in number[i]]

    number[0] = [75]

    # counter for counting number of iterations
    counter = 0

    # for loop for bottom-up approach
    for i in range(len(number) - 2, -1, -1):
        for j in range(len(number[i])):
            number[i][j] = number[i][j] + max(number[i + 1][j], number[i + 1][j + 1])
            counter += 1
        number.pop()

    # printing the output
    print(f'Found {number[0][0]} in {counter} iterations')
    end = time.time()
    print(end - start)


main()
