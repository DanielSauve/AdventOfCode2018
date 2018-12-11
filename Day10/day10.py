def find_word(stars):
    positions = []
    velocities = []
    for star in stars:
        pos = [int(star[10:16]), int(star[18:24])]
        vel = [int(star[36:38]), int(star[40:42])]
        positions.append(pos)
        velocities.append(vel)
    iterations = 1
    while True:
        for i in range(len(positions)):
            positions[i][0] += velocities[i][0]
            positions[i][1] += velocities[i][1]
        for pos in positions:
            found = 0
            for pos2 in positions:
                if pos[0] == pos2[0]:
                    if pos[1] == pos2[1] + 1:
                        found += 1
                    elif pos[1] == pos2[1] + 2:
                        found += 2
                    elif pos[1] == pos2[1] + 3:
                        found += 3
                    elif pos[1] == pos2[1] + 4:
                        found += 4
                    elif pos[1] == pos2[1] + 5:
                        found += 5
            if found == 15:
                output = [["." for _ in range(500)] for _ in range(500)]
                for position in positions:
                    output[position[1]][position[0]] = "#"
                out_file = open(str(iterations) + ".txt", "w")
                for row in output:
                    for c in row:
                        out_file.write(c)
                    out_file.write("\n")
                break
        iterations += 1
        if iterations > 11000:
            break


if __name__ == "__main__":
    problem_input = open("./day10.txt").read()
    find_word(problem_input.split("\n"))
