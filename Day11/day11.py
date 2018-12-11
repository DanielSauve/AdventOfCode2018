def most_power(serial_number):
    grid = [[power_level(x, y, serial_number) for x in range(300)] for y in range(300)]
    max_found = -100
    location = (0, 0)
    for y in range(len(grid) - 3):
        for x in range(len(grid[y]) - 3):
            val = sum(grid[y][x:x + 3]) + sum(grid[y + 1][x:x + 3]) + sum(grid[y + 2][x:x + 3])
            if val > max_found:
                max_found = val
                location = (x, y)
    return location


def most_power_adjustable(serial_number):
    grid = [[power_level(x, y, serial_number) for x in range(300)] for y in range(300)]
    max_found = -100
    location = (0, 0, 0)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            for size in range(1, min(len(grid) - x, len(grid) - y)):
                val = 0
                for i in range(size):
                    val += sum(grid[y + i][x:x + size])
                if val > max_found:
                    max_found = val
                    location = (x, y, size)
    return location


def power_level(x, y, serial_number):
    rack_id = x + 10
    level = (rack_id * y + serial_number) * rack_id
    return ((level % 1000) // 100) - 5


if __name__ == "__main__":
    problem_input = open("day11.txt").read()
    print(most_power(int(problem_input)))
    print(most_power_adjustable(int(problem_input)))
