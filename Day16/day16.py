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


def find_opcodes(samples):
    possible_opcodes = dict()
    for i in range(16):
        possible_opcodes[i] = {"addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir",
                               "gtri", "gtrr", "eqir", "eqri", "eqrr"}
    for sample in samples:
        sample = sample.split("\n")
        before = list(map(lambda x: int(x), sample[0][9:19].split(",")))
        opcode = list(map(lambda x: int(x), sample[1].split(" ")))
        after = list(map(lambda x: int(x), sample[2][9:19].split(",")))
        if before[opcode[1]] + before[opcode[2]] != after[opcode[3]] and "addr" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("addr")
        if before[opcode[1]] + opcode[2] != after[opcode[3]] and "addi" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("addi")
        if before[opcode[1]] * before[opcode[2]] != after[opcode[3]] and "mulr" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("mulr")
        if before[opcode[1]] * opcode[2] != after[opcode[3]] and "muli" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("muli")
        if before[opcode[1]] & before[opcode[2]] != after[opcode[3]] and "banr" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("banr")
        if before[opcode[1]] & opcode[2] != after[opcode[3]] and "bani" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("bani")
        if before[opcode[1]] | before[opcode[2]] != after[opcode[3]] and "borr" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("borr")
        if before[opcode[1]] | opcode[2] != after[opcode[3]] and "bori" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("bori")
        if before[opcode[1]] != after[opcode[3]] and "setr" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("setr")
        if opcode[1] != after[opcode[3]] and "seti" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("seti")
        if opcode[1] > before[opcode[2]] and after[opcode[3]] != 1 and "gtir" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("gtir")
        if opcode[1] <= before[opcode[2]] and after[opcode[3]] != 0 and "gtir" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("gtir")
        if before[opcode[1]] > opcode[2] and after[opcode[3]] != 1 and "gtri" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("gtri")
        if before[opcode[1]] <= opcode[2] and after[opcode[3]] != 0 and "gtri" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("gtri")
        if before[opcode[1]] > before[opcode[2]] and after[opcode[3]] != 1 and "gtrr" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("gtrr")
        if before[opcode[1]] <= before[opcode[2]] and after[opcode[3]] != 0 and "gtrr" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("gtrr")
        if opcode[1] == before[opcode[2]] and after[opcode[3]] != 1 and "eqir" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("eqir")
        if opcode[1] != before[opcode[2]] and after[opcode[3]] != 0 and "eqir" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("eqir")
        if before[opcode[1]] == opcode[2] and after[opcode[3]] != 1 and "eqri" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("eqri")
        if before[opcode[1]] != opcode[2] and after[opcode[3]] != 0 and "eqri" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("eqri")
        if before[opcode[1]] == before[opcode[2]] and after[opcode[3]] != 1 and "eqrr" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("eqrr")
        if before[opcode[1]] != before[opcode[2]] and after[opcode[3]] != 0 and "eqrr" in possible_opcodes[opcode[0]]:
            possible_opcodes[opcode[0]].remove("eqrr")
    not_done = True
    to_be_removed = set()
    opcodes = [None for _ in range(16)]
    while not_done:
        not_done = False
        for i in range(16):
            if len(possible_opcodes[i]) == 1:
                to_be_removed = to_be_removed.union(possible_opcodes[i])
                (opcodes[i],) = possible_opcodes[i]
            else:
                possible_opcodes[i].difference_update(to_be_removed)
                not_done = True
    return opcodes


def run_program(opcodes, program):
    registers = [0, 0, 0, 0]
    for op in program.split("\n"):
        op = list(map(lambda x: int(x), op.split(" ")))
        if opcodes[op[0]] == "addr":
            registers[op[3]] = registers[op[1]] + registers[op[2]]
        elif opcodes[op[0]] == "addi":
            registers[op[3]] = registers[op[1]] + op[2]
        elif opcodes[op[0]] == "mulr":
            registers[op[3]] = registers[op[1]] * registers[op[2]]
        elif opcodes[op[0]] == "muli":
            registers[op[3]] = registers[op[1]] * op[2]
        elif opcodes[op[0]] == "banr":
            registers[op[3]] = registers[op[1]] & registers[op[2]]
        elif opcodes[op[0]] == "bani":
            registers[op[3]] = registers[op[1]] & op[2]
        elif opcodes[op[0]] == "borr":
            registers[op[3]] = registers[op[1]] | registers[op[2]]
        elif opcodes[op[0]] == "bori":
            registers[op[3]] = registers[op[1]] | op[2]
        elif opcodes[op[0]] == "setr":
            registers[op[3]] = registers[op[1]]
        elif opcodes[op[0]] == "seti":
            registers[op[3]] = op[1]
        elif opcodes[op[0]] == "gtir":
            registers[op[3]] = 1 if op[1] > registers[op[2]] else 0
        elif opcodes[op[0]] == "gtri":
            registers[op[3]] = 1 if registers[op[1]] > op[2] else 0
        elif opcodes[op[0]] == "gtrr":
            registers[op[3]] = 1 if registers[op[1]] > registers[op[2]] else 0
        elif opcodes[op[0]] == "eqir":
            registers[op[3]] = 1 if op[1] == registers[op[2]] else 0
        elif opcodes[op[0]] == "eqri":
            registers[op[3]] = 1 if registers[op[1]] == op[2] else 0
        elif opcodes[op[0]] == "eqrr":
            registers[op[3]] = 1 if registers[op[1]] == registers[op[2]] else 0
    return registers


if __name__ == "__main__":
    problem_input = open("./day16.txt").read()
    print(undefined_behaviour(problem_input.split("\n\n")[:-2]))
    opcodes = find_opcodes(problem_input.split("\n\n")[:-2])
    print(run_program(opcodes, problem_input.split("\n\n")[-1]))
