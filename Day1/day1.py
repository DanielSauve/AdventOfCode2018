def add_frequencies(frequencies):
    return sum(map(lambda x: int(x), frequencies))


def revisited_frequency(frequencies):
    frequencies = list(map(lambda x: int(x), frequencies))
    count = 0
    seen = set()
    seen.add(count)
    while True:
        for i in frequencies:
            count += i
            if count in seen:
                return count
            seen.add(count)


if __name__ == "__main__":
    problemInput = open("./day1.txt").read()
    print(add_frequencies(problemInput.split()))
    print(revisited_frequency(problemInput.split()))
