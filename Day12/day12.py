def number_of_plants(state, rules, generations):
    zero = 0
    for _ in range(generations):
        new_state = []
        if state[0] == '#' or state[1] == '#':
            new_state.append(rules["...." + state[0]])
            new_state.append(rules["..." + "".join(state[0:2])])
            zero += 2
        for i in range(len(state)):
            if i == 0:
                new_state.append(rules[".." + "".join(state[i:i + 3])])
            elif i == 1:
                new_state.append(rules["." + "".join(state[i - 1:i + 3])])
            elif i == len(state) - 2:
                new_state.append(rules["".join(state[i - 2:i + 2]) + "."])
            elif i == len(state) - 1:
                new_state.append(rules["".join(state[i - 2:i + 1]) + ".."])
            else:
                new_state.append(rules["".join(state[i - 2:i + 3])])
        if state[-1] == '#' or state[-2] == '#':
            new_state.append(rules["".join(state[-2:]) + "..."])
            new_state.append(rules["".join(state[-1:]) + "...."])
        state = new_state
    return pot_number_sum(state, zero)


def pot_number_sum(state, zero_location):
    count = 0
    for i in range(len(state)):
        if state[i] == '#':
            count += i - zero_location
    return count


if __name__ == "__main__":
    problem_input = open("day12.txt").read()
    problem_input = problem_input.split("\n")
    state = list(map(lambda x: x, problem_input[0].replace("initial state: ", "")))
    rules = {}
    for rule in problem_input[2:]:
        rule = rule.split(" => ")
        rules[rule[0]] = rule[1]
    print(number_of_plants(state, rules, 20))
    # For context, this only works because past generation 125 it increases by 88 each generation
    print(number_of_plants(state, rules, 200) + (50000000000 - 200) * 88)
