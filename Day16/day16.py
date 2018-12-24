def undefined_behaviour(samples):
    unknown = 0
    for sample in samples:
        count = 0
        sample = sample.split("\n")
        before = list(map(lambda x: int(x), sample[0][9:19].split(",")))
        opcode = list(map(lambda x: int(x), sample[1].split(" ")))
        after = list(map(lambda x: int(x), sample[2][9:19].split(",")))
        if before[opcode[1]] + before[opcode[2]] == after[opcode[3]]:
            count += 1
        if before[opcode[1]] + opcode[2] == after[opcode[3]]:
            count += 1
        if before[opcode[1]] * before[opcode[2]] == after[opcode[3]]:
            count += 1
        if before[opcode[1]] * opcode[2] == after[opcode[3]]:
            count += 1
        if before[opcode[1]] & before[opcode[2]] == after[opcode[3]]:
            count += 1
        if before[opcode[1]] & opcode[2] == after[opcode[3]]:
            count += 1
        if before[opcode[1]] | before[opcode[2]] == after[opcode[3]]:
            count += 1
        if before[opcode[1]] | opcode[2] == after[opcode[3]]:
            count += 1
        if before[opcode[1]] == after[opcode[3]]:
            count += 1
        if opcode[1] == after[opcode[3]]:
            count += 1
        if opcode[1] > before[opcode[2]]:
            count += 1 if after[opcode[3]] == 1 else 0
        else:
            count += 1 if after[opcode[3]] == 0 else 0
        if before[opcode[1]] > opcode[2]:
            count += 1 if after[opcode[3]] == 1 else 0
        else:
            count += 1 if after[opcode[3]] == 0 else 0
        if before[opcode[1]] > before[opcode[2]]:
            count += 1 if after[opcode[3]] == 1 else 0
        else:
            count += 1 if after[opcode[3]] == 0 else 0
        if opcode[1] == before[opcode[2]]:
            count += 1 if after[opcode[3]] == 1 else 0
        else:
            count += 1 if after[opcode[3]] == 0 else 0
        if before[opcode[1]] == opcode[2]:
            count += 1 if after[opcode[3]] == 1 else 0
        else:
            count += 1 if after[opcode[3]] == 0 else 0
        if before[opcode[1]] == before[opcode[2]]:
            count += 1 if after[opcode[3]] == 1 else 0
        else:
            count += 1 if after[opcode[3]] == 0 else 0
        if count >= 3:
            unknown += 1
    return unknown


if __name__ == "__main__":
    problem_input = open("./day16.txt").read()
    print(undefined_behaviour(problem_input.split("\n\n")[:-2]))
