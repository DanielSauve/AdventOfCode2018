def requirements_to_steps(requirements):
    steps = {}
    for req in requirements:
        req = req.split()
        first = req[1]
        second = req[7]
        if second in steps.keys():
            steps[second].append(first)
            steps[second].sort()
        else:
            steps[second] = [first]
        if first not in steps.keys():
            steps[first] = []
    return steps


def step_order(requirements):
    steps = requirements_to_steps(requirements)
    sequence = []
    done = False
    while not done:
        c = ord('Z') + 1
        for d in steps.keys():
            if len(steps[d]) == 0 and ord(d) < c:
                c = ord(d)
        c = chr(c)
        del steps[c]
        sequence.append(c)
        for d in steps:
            if c in steps[d]:
                steps[d].remove(c)
        if len(steps.keys()) == 0:
            done = True
    return ''.join(sequence)


def total_duration(requirements):
    steps = requirements_to_steps(requirements)
    time_remaining = {}
    for c in steps.keys():
        time_remaining[c] = ord(c) - ord('A') + 61
    workers = [None for _ in range(5)]
    time = 0
    done = False
    while not done:
        possibilities = []
        for c in steps.keys():
            if len(steps[c]) == 0:
                possibilities.append(c)
        possibilities.sort(reverse=True)
        for i in range(len(workers)):
            if workers[i] is None and len(possibilities) != 0:
                workers[i] = possibilities.pop()
                del steps[workers[i]]
            if workers[i] is not None:
                time_remaining[workers[i]] -= 1
                if time_remaining[workers[i]] == 0:
                    for c in steps.keys():
                        if workers[i] in steps[c]:
                            steps[c].remove(workers[i])
                    workers[i] = None
        time += 1
        workers_done = True
        for worker in workers:
            if worker is not None:
                workers_done = False
        if len(steps.keys()) == 0 and workers_done:
            done = True
    return time


if __name__ == "__main__":
    problemInput = open("./day7.txt").read()
    print(step_order(problemInput.split("\n")))
    print(total_duration(problemInput.split("\n")))
