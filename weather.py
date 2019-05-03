import sys
import re


def minimum_spread(filename):
    lines = tuple(open(FILENAME, "r"))
    min_spread = sys.maxsize
    min_day = 0
    FORMAT = 2
    DAY = 0
    MAX_TEMP = 1
    MIN_TEMP = 2

    for line in lines:
        new_line = re.findall(r"\d+", line)

        if len(new_line) > FORMAT:
            difference = abs(int(new_line[MAX_TEMP]) - int(new_line[MIN_TEMP]))

            if difference < min_spread:
                min_spread = difference
                min_day = new_line[DAY]

    print("day with minimum temp spread: ", min_day)


if __name__ == "__main__":
    FILENAME = "w_data (5).dat"
    minimum_spread(FILENAME)
