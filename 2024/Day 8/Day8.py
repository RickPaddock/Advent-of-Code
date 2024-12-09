from itertools import combinations

with open('./input data/source_input.txt', 'r') as f:
    grid = [line.strip() for line in f.readlines()]

print(grid)

MAX_X = len(grid[0])
MAX_Y = len(grid) 


def is_in_grid(loc):
    x,y = loc[0], loc[1]
    return x >= 0 and x < MAX_X and y >= 0 and y < MAX_Y


# Create dict of items (those that don't = '.') and their locations
item_locations = {}
[item_locations.setdefault(x_val, []).append((x_loc, y_loc)) for y_loc, y_val in enumerate(grid) for x_loc, x_val in enumerate(y_val) if x_val != "."]
print("item_locations", item_locations)


# All similar items grouped together in twos, so we can find all possible combinations
all_combos = {key: set() for key in item_locations.keys()}
for key, value in item_locations.items():
    all_combos[key] = set(combinations(value, r=2))
#print("all_combos", all_combos)


# Work out all positive and negative directions for every difference
antinodes = {key: set() for key in item_locations.keys()}
for key, value in all_combos.items():
    value_lst = list(value)
    for val in value_lst:
        (x1, y1), (x2, y2) = val
        dx, dy = x1 - x2, y1 - y2

        # Calculate all potential positions
        potential_positions = [
            (x1 + dx, y1 + dy),  # Positive direction for first point
            (x1 - dx, y1 - dy),  # Negative direction for first point
            (x2 + dx, y2 + dy),  # Positive direction for second point
            (x2 - dx, y2 - dy),  # Negative direction for second point
        ]

        # Add valid positions to antinodes
        for pos in potential_positions:
            if is_in_grid(pos):
                antinodes[key].add(pos)


# Flatten all item locations into a single set
all_item_locations = {loc for locations in item_locations.values() for loc in locations}
#print("all_item_locations", all_item_locations)

# Filter antinodes regardless of the key
result = [(k, {node for node in v if node not in item_locations[k]}) for k, v in antinodes.items()]

# Count unique (x, y) values across all keys in `result`
unique_values = set()
for _, nodes in result:
    unique_values.update(nodes)

print("Answer A:", len(unique_values))

