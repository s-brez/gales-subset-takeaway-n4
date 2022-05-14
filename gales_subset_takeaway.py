from itertools import combinations

n = 6


def complement(universal_set: set, E: set):
    """
    Returns list of elements not in E that exist in the universal set
    """
    return universal_set - E


# Create fixed finite sets from 1 through n
sets = {}
for i in range(n):
    sets[i + 1] = [j + 1 for j in range(i + 1)]

# Find all valid first moves for games of each set size
valid_first_moves = {key: [] for key in sets}
for E in enumerate(sets):
    print("Game", str(str(E[1]) + ","), "where E =", set(sets[E[1]]))

    if len(sets[E[1]]) > 0:
        # print(len(sets[starting_set[1]]))

        # E = 1 is a win by default
        if len(sets[E[1]]) == 1:
            print("E = [1], therefore player two wins by default\n")

        # All other E sizes greater than 0
        else:
            moves = []
            for r in range(len(sets[E[1]]) + 1):
                for combination in combinations(set(sets[E[1]]), r):
                    moves.append(set(combination))

            # trim empty set and entire E from moves
            del moves[0]
            del moves[-1]
            print("Valid first move sets:   ", moves)

            # get counter moves
            counters = []
            for move in moves:
                counters.append(complement(set(sets[E[1]]), move))

            print("Countering 2nd move sets:", counters, "\n")
