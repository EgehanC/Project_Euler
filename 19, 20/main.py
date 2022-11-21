import datetime
from math import factorial


def count_first_sundays():
    sundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            day = datetime.date(year, month, 1)
            if day.weekday() == 6:
                sundays += 1

    print(f"Sundays: {sundays}")


# count_first_sundays()


def dig_sum():
    n = 100
    fact_n = factorial(n)

    str_fact_n = str(fact_n)
    sum = 0
    for i in str_fact_n:
        sum += int(i)

    print(sum)

# dig_sum()
