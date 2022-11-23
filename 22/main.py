from names import names
import time

alphabet = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}


def main():
    start = time.time()
    # formatting the list
    for i in range(len(names)):
        names[i] = names[i].lower()

    # sorting the list
    sorted_names = sorted(names)
    sum = 0
    index = 1
    for name in sorted_names:
        name_score = 0
        for letter in name:
            name_score += alphabet[letter]
        name_score *= index
        index += 1
        sum += name_score

    end = time.time()
    print(f"Sum of all name scores: {sum}")
    print(f"Time: {round(end - start, 6)}")


main()
