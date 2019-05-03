import sys
import re


def smallest_difference(filename):
    lines = tuple(open(filename, "r"))
    min_difference = sys.maxsize
    end_team = ""
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
                end_team = new_line[TEAM]

    print("team with smallest difference: ", end_team)


if __name__ == "__main__":
    FILENAME = "soccer.dat"
    smallest_difference(FILENAME)
