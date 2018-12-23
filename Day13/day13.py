class Cart:
    def __init__(self, pos_x, pos_y, direction):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = direction
        self.turn_count = 0


def collision_position(tracks):
    tracks = list(map(lambda x: list(x), tracks.split("\n")))
    carts = []
    prev = set()
    for y in range(len(tracks)):
        for x in range(len(tracks[y])):
            c = tracks[y][x]
            if c == "^":
                carts.append(Cart(x, y, 0))
                prev.add((x, y))
                tracks[y][x] = "|"
            elif c == "<":
                carts.append(Cart(x, y, 3))
                prev.add((x, y))
                tracks[y][x] = "-"
            elif c == ">":
                carts.append(Cart(x, y, 1))
                prev.add((x, y))
                tracks[y][x] = "-"
            elif c == "v":
                carts.append(Cart(x, y, 2))
                prev.add((x, y))
                tracks[y][x] = "|"
    while True:
        curr = set()
        for cart in carts:
            prev.remove((cart.pos_x, cart.pos_y))
            cart.pos_y += 1 if cart.direction == 2 else -1 if cart.direction == 0 else 0
            cart.pos_x += 1 if cart.direction == 1 else -1 if cart.direction == 3 else 0
            if (cart.pos_x, cart.pos_y) in prev or (cart.pos_x, cart.pos_y) in curr:
                return cart.pos_x, cart.pos_y
            curr.add((cart.pos_x, cart.pos_y))
            if tracks[cart.pos_y][cart.pos_x] == "\\":
                cart.direction += 1 if cart.direction % 2 == 1 else -1
            elif tracks[cart.pos_y][cart.pos_x] == "/":
                cart.direction += 1 if cart.direction % 2 != 1 else -1
            elif tracks[cart.pos_y][cart.pos_x] == "+":
                cart.direction += 1 if cart.turn_count == 2 else 0 if cart.turn_count == 1 else -1
                cart.turn_count = (cart.turn_count + 1) % 3
            cart.direction = cart.direction % 4
        prev = curr
        carts.sort(key=lambda cart: (cart.pos_y, cart.pos_x))


def last_cart(tracks):
    tracks = list(map(lambda x: list(x), tracks.split("\n")))
    carts = []
    prev = set()
    for y in range(len(tracks)):
        for x in range(len(tracks[y])):
            c = tracks[y][x]
            if c == "^":
                carts.append(Cart(x, y, 0))
                prev.add((x, y))
                tracks[y][x] = "|"
            elif c == "<":
                carts.append(Cart(x, y, 3))
                prev.add((x, y))
                tracks[y][x] = "-"
            elif c == ">":
                carts.append(Cart(x, y, 1))
                prev.add((x, y))
                tracks[y][x] = "-"
            elif c == "v":
                carts.append(Cart(x, y, 2))
                prev.add((x, y))
                tracks[y][x] = "|"
    while len(carts) > 1:
        curr = set()
        collisions = set()
        for cart in carts:
            prev.remove((cart.pos_x, cart.pos_y))
            if (cart.pos_x, cart.pos_y) in collisions:
                continue
            cart.pos_y += 1 if cart.direction == 2 else -1 if cart.direction == 0 else 0
            cart.pos_x += 1 if cart.direction == 1 else -1 if cart.direction == 3 else 0
            if (cart.pos_x, cart.pos_y) in prev or (cart.pos_x, cart.pos_y) in curr:
                collisions.add((cart.pos_x, cart.pos_y))
            curr.add((cart.pos_x, cart.pos_y))
            if tracks[cart.pos_y][cart.pos_x] == "\\":
                cart.direction += 1 if cart.direction % 2 == 1 else -1
            elif tracks[cart.pos_y][cart.pos_x] == "/":
                cart.direction += 1 if cart.direction % 2 != 1 else -1
            elif tracks[cart.pos_y][cart.pos_x] == "+":
                cart.direction += 1 if cart.turn_count == 2 else 0 if cart.turn_count == 1 else -1
                cart.turn_count = (cart.turn_count + 1) % 3
            cart.direction = cart.direction % 4
        prev = curr
        if len(collisions) > 0:
            carts = list(filter(lambda x: (x.pos_x, x.pos_y) not in collisions, carts))
            for pos in collisions:
                prev.remove(pos)
        carts.sort(key=lambda cart: (cart.pos_y, cart.pos_x))
    return carts[0].pos_x, carts[0].pos_y


if __name__ == "__main__":
    problem_input = open("day13.txt").read()
    print(collision_position(problem_input))
    print(last_cart(problem_input))
