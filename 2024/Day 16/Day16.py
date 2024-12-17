# This one took some effort! Never attempted route finder code before.
# I used a simple stack approach which worked well for the small examples but was really
# inefficienct for the large maze. Researched heapq & 'Manhattan distance' scoring which seems to work.
# Doubt it's the most efficient though.  Finding all paths for part B slowest it right down.

# It checks the score up until any given point, and only checks other paths from that point if they
# arrived with the same or lower score. Priority for the next checked path is the closet to the exit.
# 1st to exit creates 'best_score' which prevents all other attempts if they are > best_score.

from heapq import heappop, heappush # Required for stack path priority

with open(f"./input data/source_input.txt", 'r') as f:
    maze = [line.strip() for line in f.readlines() if line.strip()]

# x,y cordinates of all spaces in the maze
spaces = [(n_x,n_y) for n_y,y in enumerate(maze) for n_x,x in enumerate(y) if x in("S","E",".")]


def look_around(pos):
    """ Check up down left right from given position """
    x, y = pos
    return [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]


def find_start_end(input):
    """Return (x, y) locations of all occurrences of item."""
    start_xy, end_xy = None, None
    for y, row in enumerate(input):
        for x, val in enumerate(row):
            if val == "S":
                start_xy = (x, y)
            elif val == "E":
                end_xy = (x, y)
    return start_xy, end_xy


def calculate_score(path, start):
    """ Calculate the score for a given path """
    score = len(path) - 1  # Base score: 1 per move
    # Apply 1000 penalty for the first move if it doesn't go east
    if len(path) > 1:
        start_x, start_y = start
        first_x, first_y = path[1]
        if first_x != start_x + 1 or first_y != start_y:
            score += 1000  
    # Apply 1000 penalty for any turn
    for i in range(2, len(path)):
        prev_x, prev_y = path[i - 2]
        curr_x, curr_y = path[i - 1]
        next_x, next_y = path[i]
        # A turn occurs if the direction of movement changes
        if (curr_x - prev_x != next_x - curr_x) or (curr_y - prev_y != next_y - curr_y):
            score += 1000  # Penalty for a turn
    return score


def exit_score(current_xy, exit_xy):
    """ Manhattan Distance score. Shortest distance from current location to exit """
    # 0 = x & 1 = y
    return abs(current_xy[0] - exit_xy[0]) + abs(current_xy[1] - exit_xy[1])


def find_best_route(spaces, start, end):
    """ Find the most efficient route from start to end """
    # Priority queue: (priority, current position, path)
    # In a heap, the element with the smallest value hs highest priority & goes to front of queue
    pq = []
    heappush(pq, (0, start, [start]))
    
    visited = {} # Dict to check any location & the smallest score to get there
    best_score = float('inf') # Start best score as super high (infinitiy)
    all_paths = []

    while pq:
        # Extract the path with the lowest score
        current_priority, current_pos, path = heappop(pq)
        current_score = calculate_score(path, start)

        # If we've already visited with a better score, skip
        # PartB required ALL best paths so +1001 here to check paths which turn on arrival (INEFFICIENT!)
        if current_pos in visited and visited[current_pos] +1001 <= current_score:
            continue
        visited[current_pos] = current_score

        # If we reach the end, check if it's the best score
        if current_pos == end:
            if current_score <= best_score:
                best_score = current_score
                all_paths.append(path)
            continue  # Continue exploring to collect all best paths

        # Explore neighbors
        for direction_xy in look_around(current_pos):
            if direction_xy in spaces and direction_xy not in path:
                new_path = path + [direction_xy]
                # Push new path to check. Lowest score has priority & is processed next
                new_priority = calculate_score(new_path, start) + exit_score(direction_xy, end)
                heappush(pq, (new_priority, direction_xy, new_path))

    return all_paths, best_score


start, end = find_start_end(maze)
# find all best paths and with the smallest score
all_paths, score = find_best_route(spaces, start, end)

print(f"PART A: Lowest Score: {score}")
unique_locations = list(set(path for single_path in all_paths for path in single_path))
print(f"PART B: Unique locations for all paths with lowest score: {len(unique_locations)}")

#Print final maze for ALL lowest score paths so we can see in what areas they diverged
maze2 = [list(row) for row in maze]
updated_maze = ""
for path_xy in unique_locations:
    maze2[path_xy[1]][path_xy[0]] = 'O'
    updated_maze = '\n'.join(''.join(row) for row in maze2)
print("Routes of ALL paths with the lowest score")
print(updated_maze)
