with open('./input data/source_input.txt', 'r') as f:
    topography = [line.strip() for line in f.readlines()]


MAX_X = len(topography[0]) 
MAX_Y = len(topography)

# up,down,left,right
directions = [(0,-1),(0,1),(-1,0),(1,0)]


def find_start(input, item):
    """ Return (x,y) locations of all occurances of item """
    start_points = []
    for y, str in enumerate(input):
        for x, val in enumerate(str):
            if val == item:
                start_points.append((x,y))
    return start_points 


def is_in_grid(loc):
    """ Return True if (x,y) is within boundaries, False if not """
    x,y = loc[0], loc[1]
    return x >= 0 and x< MAX_X and y >= 0 and y < MAX_Y


def look_around(loc):
    """ Return (x,y) cordinates of all 4 surrounding locations """
    x,y = loc[0], loc[1]
    result = []
    for i in directions:
        result.append((x+int(i[0]), y+int(i[1])))
    return result


def find_all_routes(grid, start):
    """ Find all routes from 0->9 using stack """
    # Stack holds current location and list of visited location
    stack = [(start, [start])]
    success_routes = []
    while stack:
        # Extract latest stack record (current location and route completed thus far)
        (x, y), path = stack.pop()
        # Exit if 9 is in current location. Entry has been popped from stack
        if grid[y][x] == "9":
            success_routes.append(path)
            continue
        # Explore all possible moves from current poisition
        for direction_xy in look_around((x, y)):
            if is_in_grid(direction_xy) and direction_xy not in path:
                if grid[direction_xy[1]][direction_xy[0]] != ".": # This line only required for testing
                    # Append new found path from current location if number is +1
                    if int(grid[direction_xy[1]][direction_xy[0]]) == int(grid[y][x])+1:
                        stack.append(((direction_xy), path + [(direction_xy)]))

    return success_routes


start_points = find_start(topography, "0")
unique_start_end = set() # Unique start/end positions
total_paths = []

for sp_xy in start_points:
    paths = find_all_routes(topography, sp_xy)
    for path in paths:
        unique_start_end.add((path[0],path[-1]))
        total_paths.append(path)


print("Answer A:", len(unique_start_end))
print("Answer B:", len(total_paths))
