def top_ten_after(after):
    recipes = [3, 7]
    elf_one, elf_two = 0, 1
    iteration = 1
    while iteration < after + 9:
        next_val = recipes[elf_one] + recipes[elf_two]
        if next_val >= 10:
            recipes.append(next_val // 10)
            recipes.append(next_val % 10)
            iteration += 2
        else:
            recipes.append(next_val)
            iteration += 1
        elf_one = (elf_one + recipes[elf_one] + 1) % len(recipes)
        elf_two = (elf_two + recipes[elf_two] + 1) % len(recipes)
    return recipes[-10:]


def number_before(before):
    recipes = [3, 7]
    elf_one, elf_two = 0, 1
    while True:
        if len(recipes) >= len(before):
            match = True
            for i in range(len(before)):
                if int(before[i]) != recipes[-len(before) + i]:
                    match = False
            if match:
                return len(recipes) - len(before)
        next_val = recipes[elf_one] + recipes[elf_two]
        if next_val >= 10:
            recipes.append(next_val // 10)
            recipes.append(next_val % 10)
        else:
            recipes.append(next_val)
        elf_one = (elf_one + recipes[elf_one] + 1) % len(recipes)
        elf_two = (elf_two + recipes[elf_two] + 1) % len(recipes)


if __name__ == "__main__":
    problem_input = open("day14.txt").read()
    print("".join(map(lambda x: str(x), top_ten_after(int(problem_input)))))
    print(number_before(problem_input))
