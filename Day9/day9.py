def winning_player(num_players, last_marble):
    marbles = [0]
    scores = [0 for _ in range(num_players)]
    turn_count = 1
    curr_pos = 1
    done = False
    while not done:
        if turn_count % 23 != 0:
            marbles.insert(curr_pos, turn_count)
            turn_count += 1
            curr_pos += 2
            curr_pos = curr_pos % len(marbles)
        else:
            value = turn_count + marbles[curr_pos - 9]
            print(value)
            marbles.pop(curr_pos - 9)
            curr_pos -= 7
            scores[turn_count % num_players] += value
            turn_count += 1
        if turn_count == last_marble + 1:
            break
    return max(scores)


if __name__ == "__main__":
    problem_input = open("day9.txt").read()
    problem_input = problem_input.split()
    players = int(problem_input[0])
    worth = int(problem_input[6])
    print(winning_player(players, worth))
    # print(winning_player(players, worth * 100))
