import sys
sys.setrecursionlimit(8000) # So recursive function call works with big grids!

with open('./input data/source_input.txt', 'r') as f:
    main_grid = [line.strip() for line in f.readlines()]

obstacle_locs = set([(x, y) for y, y_val in enumerate(main_grid) for x, x_val in enumerate(y_val) if x_val == '#'])
print(obstacle_locs)

MAX_X = len(main_grid[0]) 
MAX_Y = len(main_grid) 

def print_grid(grid):
    for i in grid:
        print(i)

print("Start Grid")
print_grid(main_grid)

# Cordinates of new position per icon. Keys are in order of turning right
directions = {"^": (0,-1),">":(1,0),"v":(0,1),"<":(-1,0)}

previous_visits = {key: set() for key in directions.keys()}

count_infinate_loop = [0]


def find_start(input, guard):
    for y, str in enumerate(input):
        for x, val in enumerate(str):
            if val == guard:
                return x,y

def turn_right(guard):
    """ Obtain next 'turn right' icon from dict """
    # Get next guard icon from dict. They are in order of turning right
    direction_index = [*directions].index(guard)+1
    direction_index = 0 if direction_index >= len(directions) else direction_index
    new_guard_direction = list(directions)[direction_index]
    return new_guard_direction


def look_forward(loc, facing):
    x,y = loc[0], loc[1]
    x_move, y_move = directions[facing]
    return x+x_move,y+y_move


def is_in_grid(loc):
    x,y = loc[0], loc[1]
    return x >= 0 and x< MAX_X and y >= 0 and y < MAX_Y


def capture_visit(loc, guard):
    previous_visits[guard].add(loc)


def is_infinate_loop(loc, guard):
    return loc in previous_visits[guard]


def move(obstacles, current_loc, guard, cumulative_infinate=[0]):
    while True: 
        fwd_loc = look_forward(current_loc, guard)
        if not is_in_grid(fwd_loc):
            capture_visit(current_loc, guard)
            break
        
        # Handle obstacle detection
        turn_count = 0
        while fwd_loc in obstacles:
            guard = turn_right(guard)
            fwd_loc = look_forward(current_loc, guard)
            turn_count += 1
            if turn_count == 4:  # 4 turns means a full circle (right turn 4 times)
                print("Stuck in full circle!")
                return
        
        # Check for infinite loop
        if is_infinate_loop(current_loc, guard):
            cumulative_infinate[0] += 1
            #print("Infinite loop", cumulative_infinate)
            break
        
        capture_visit(current_loc, guard)
        current_loc = fwd_loc  # Move forward



start_guard = "^"
start_loc = find_start(main_grid, start_guard)
print("start cordinates:", start_loc, start_guard)

move(obstacle_locs, start_loc, start_guard)

unique_locs = set(loc for visits in previous_visits.values() for loc in visits)
print("ANSWER PART A:", len(unique_locs))


cumulative_infinate = [0]
for loc in unique_locs: 
    if loc == start_loc:  # Skip if it's the start guard location
        continue
    previous_visits = {key: set() for key in directions.keys()}
    # Add new obstacle to one of the previously visited locations, move, then remove obstacle
    obstacle_locs.add(loc) 
    move(obstacle_locs, start_loc, start_guard, cumulative_infinate)
    obstacle_locs.remove(loc)


print("ANSWER PART B:", cumulative_infinate[0])