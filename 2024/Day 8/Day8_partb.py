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
potential_positions = []
for key, value in all_combos.items():
    value_lst = list(value)
    print("KEY", key, value_lst)
    for val in value_lst:
        #print("val", val)
        (x1, y1), (x2, y2) = val
        dx, dy = x1 - x2, y1 - y2

        ### A FUDGE FOR PART B - needs refactoring!!! ###
        # Applying dx,dy needs repeating till end (NOT is_in_grid())
        pos = (x1 + dx, y1 + dy)
        for i in val[0]:
            potential_positions.append((x1, y1))
            potential_positions.append((x2, y2))
            potential_positions.append(pos)
            # Apply same positive distance until they leave the grid
            while is_in_grid(pos):
                pos = (pos[0] + dx, pos[1] + dy)
                potential_positions.append(pos)
        neg = (x1 - dx, y1 - dy)
        for i in val[0]:
            potential_positions.append(neg)
            # Apply same negative distance until they leave the grid
            while is_in_grid(neg):
                neg = (neg[0] - dx, neg[1] - dy)
                potential_positions.append(neg)

        #print("potential_positions", potential_positions)

        # Add valid positions to antinodes
        for pos in potential_positions:
            if is_in_grid(pos):
                antinodes[key].add(pos)


# Flatten all item locations into a single set
all_item_locations = {loc for locations in item_locations.values() for loc in locations}
#print("all_item_locations", all_item_locations)

# Filter antinodes regardless of the key
result = [(k, {node for node in v}) for k, v in antinodes.items()]


# Count unique (x, y) values across all keys in `result`
unique_values = set()
for _, nodes in result:
    unique_values.update(nodes)

print("Answer B:", len(unique_values))

