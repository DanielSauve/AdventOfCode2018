import re


def checksum(ids):
    two_count = 0
    three_count = 0
    two_regex = r"(.)(.*\1){1}"
    three_regex = r"(.).*\1.*\1"
    for line in ids:
        if re.search(two_regex, line):
            two_count += 1
        if re.search(three_regex, line):
            three_count += 1
    return two_count * three_count


if __name__ == "__main__":
    problemInput = open("./day2.txt").read()
    print(checksum(problemInput.split()))


