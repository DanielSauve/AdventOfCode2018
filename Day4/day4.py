import re


def longest_sleeper(notes):
    notes.sort()
    total_sleep = {}
    minute_sleep = {}
    time_regex = re.compile("(\d\d):(\d\d)")
    guard, start = -1, -1
    for note in notes:
        if "begins shift" in note:
            guard = int(note.split()[3].replace("#", ""))
            start = -1
        elif "falls asleep" in note:
            start = int(time_regex.search(note).group(2))
        elif "wakes up" in note:
            end = int(time_regex.search(note).group(2))
            if guard not in total_sleep.keys():
                total_sleep[guard] = end - start
            else:
                total_sleep[guard] += end - start
            for minute in range(start, end):
                if (guard, minute) not in minute_sleep.keys():
                    minute_sleep[(guard, minute)] = 1
                else:
                    minute_sleep[(guard, minute)] += 1
            start = -1
    max_sleep = -1
    for key in total_sleep.keys():
        if total_sleep[key] > max_sleep:
            max_sleep = total_sleep[key]
            guard = key
    max_sleep = -1
    minute = -1
    for key in minute_sleep.keys():
        if key[0] == guard and minute_sleep[key] > max_sleep:
            max_sleep = minute_sleep[key]
            minute = key[1]
    return guard * minute


def most_consistent(notes):
    notes.sort()
    minute_sleep = {}
    time_regex = re.compile("(\d\d):(\d\d)")
    guard, start = -1, -1
    for note in notes:
        if "begins shift" in note:
            guard = int(note.split()[3].replace("#", ""))
            start = -1
        elif "falls asleep" in note:
            start = int(time_regex.search(note).group(2))
        elif "wakes up" in note:
            end = int(time_regex.search(note).group(2))
            for minute in range(start, end):
                if (guard, minute) not in minute_sleep.keys():
                    minute_sleep[(guard, minute)] = 1
                else:
                    minute_sleep[(guard, minute)] += 1
            start = -1
    max_sleep = -1
    minute = -1
    for key in minute_sleep.keys():
        if minute_sleep[key] > max_sleep:
            max_sleep = minute_sleep[key]
            guard = key[0]
            minute = key[1]
    return guard * minute


if __name__ == "__main__":
    problemInput = open("./day4.txt").read()
    print(longest_sleeper(problemInput.split("\n")))
    print(most_consistent(problemInput.split("\n")))
