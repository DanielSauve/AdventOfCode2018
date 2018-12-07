def largest_area(coordinates):
    coordinates = list(map(lambda x: (int(x.split(',')[0]), int(x.split(" ")[1])), coordinates))
    max_x = 0
    max_y = 0
    for point in coordinates:
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]
    areas = {}
    for point in coordinates:
        areas[point] = 0
    for x in range(-2 * max_x, 2 * max_x):
        for y in range(-2 * max_y, 2 * max_y):
            min_distance = 9999
            coord = ()
            for point in coordinates:
                dist = manhattan_distance(point, (x, y))
                if dist < min_distance:
                    min_distance = dist
                    coord = point
                elif dist == min_distance:
                    coord = None
            if coord is not None:
                areas[coord] += 1
    print(areas)


def smallest_distance(coordinates):
    coordinates = list(map(lambda x: (int(x.split(',')[0]), int(x.split(" ")[1])), coordinates))
    max_x = 0
    max_y = 0
    for point in coordinates:
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]
    size = 0
    for x in range(max_x):
        for y in range(max_y):
            count = 0
            for point in coordinates:
                count += manhattan_distance(point, (x, y))
            if count < 10000:
                size += 1
    return size


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


if __name__ == "__main__":
    problemInput = open("./day6.txt").read()
    # largest_area(problemInput.split("\n"))
    print(smallest_distance(problemInput.split("\n")))
