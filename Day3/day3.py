def overlap(instructions):
    fabric = [[0 for _ in range(1000)] for _ in range(1000)]
    for instruction in instructions:
        parsed = instruction.split()
        start = list(map(lambda x: int(x), parsed[2].replace(":", "").split(",")))
        amount = list(map(lambda x: int(x), parsed[3].split("x")))
        for i in range(start[0], start[0] + amount[0]):
            for j in range(start[1], start[1] + amount[1]):
                fabric[i][j] += 1
    count = 0
    for row in fabric:
        for tile in row:
            if tile > 1:
                count += 1
    return count


def no_overlap(instructions):
    fabric = [[0 for _ in range(1000)] for _ in range(1000)]
    for instruction in instructions:
        parsed = instruction.split()
        start = list(map(lambda x: int(x), parsed[2].replace(":", "").split(",")))
        amount = list(map(lambda x: int(x), parsed[3].split("x")))
        for i in range(start[0], start[0] + amount[0]):
            for j in range(start[1], start[1] + amount[1]):
                fabric[i][j] += 1
    for instruction in instructions:
        parsed = instruction.split()
        start = list(map(lambda x: int(x), parsed[2].replace(":", "").split(",")))
        amount = list(map(lambda x: int(x), parsed[3].split("x")))
        over = False
        for i in range(start[0], start[0] + amount[0]):
            for j in range(start[1], start[1] + amount[1]):
                if fabric[i][j] > 1:
                    over = True
        if not over:
            return parsed[0]
    return 0


if __name__ == "__main__":
    problemInput = open("./day3.txt").read()
    print(overlap(problemInput.split("\n")))
    print(no_overlap(problemInput.split("\n")))
