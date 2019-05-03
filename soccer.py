import sys
import re


def smallest_difference(filename):
    lines = tuple(open(filename, "r"))
    min_difference = sys.maxsize
    result = ""
    FORMAT = 9
    TEAM = 1
    FOR = 6
    AGAINST = 7

    for line in lines:
        new_line = re.findall(r"\w+", line)

        if len(new_line) == FORMAT:
            difference = abs(int(new_line[FOR]) - int(new_line[AGAINST]))

            if difference < min_difference:
                min_difference = difference
                result = new_line[TEAM]

    print("team with smallest difference: ", result)


if __name__ == "__main__":
    FILENAME = "soccer.dat"
    smallest_difference(FILENAME)
