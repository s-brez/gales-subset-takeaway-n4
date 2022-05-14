
n = 4

# Create fixed finite sets from 1 through n
sets = {}
for i in range(n):
	sets[i + 1] = [j + 1 for j in range(i + 1)]

# Find all valid first moves for each set size
valid_first_moves = {key: [] for key in sets}
