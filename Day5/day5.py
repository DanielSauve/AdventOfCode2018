from string import ascii_lowercase


def remaining_units(polymer):
    done = False
    skip = False
    while not done:
        new_polymer = []
        done = True
        for i in range(len(polymer) - 1):
            if skip:
                skip = False
                continue
            if polymer[i] != polymer[i + 1] and polymer[i].lower() == polymer[i + 1].lower():
                done = False
                skip = True
                continue
            else:
                new_polymer.append(polymer[i])
        new_polymer.append(polymer[len(polymer) - 1])
        skip = False
        polymer = ''.join(new_polymer)
    return len(polymer)


def collapse_polymer(polymer):
    lengths = {}
    for character in ascii_lowercase:
        lengths[character] = remaining_units(polymer.replace(character, '').replace(character.upper(), ''))
    min_length = len(polymer)
    for key in lengths.keys():
        if lengths[key] < min_length:
            min_length = lengths[key]
    return min_length


if __name__ == "__main__":
    problemInput = open("./day5.txt").read()
    print(remaining_units(problemInput))
    print(collapse_polymer(problemInput))
