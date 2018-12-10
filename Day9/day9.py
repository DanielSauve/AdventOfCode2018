class Node:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next


def winning_player(num_players, last_marble):
    circle = Node(0, None, None)
    circle.next = circle
    circle.prev = circle
    scores = [0 for _ in range(num_players)]
    turn_count = 1
    while turn_count <= last_marble:
        if turn_count % 23 != 0:
            curr = Node(turn_count, circle, circle.next)
            circle.next.prev = curr
            circle.next = curr
            circle = curr.next
            turn_count += 1
        else:
            for _ in range(8):
                circle = circle.prev
            value = turn_count + circle.val
            prev = circle.prev
            prev.next = circle.next
            prev.next.prev = prev
            circle = prev.next.next
            scores[turn_count % num_players] += value
            turn_count += 1
    return max(scores)


if __name__ == "__main__":
    problem_input = open("day9.txt").read()
    problem_input = problem_input.split()
    players = int(problem_input[0])
    worth = int(problem_input[6])
    print(winning_player(players, worth))
    print(winning_player(players, worth * 100))
