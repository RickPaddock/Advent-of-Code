import sys
sys.setrecursionlimit(6000) # So recursive function call works with big grids!


with open('./input data/source_input.txt', 'r') as f:
    grid = [line.strip() for line in f.readlines()]


def find_start(input):
    for y, str in enumerate(input):
        for x, val in enumerate(str):
            if val == "^":
                return x,y
            

# Cordinates of new position per icon. Keys are in order of turning right
directions = {"^": (0,-1),">":(1,0),"v":(0,1),"<":(-1,0)}


def move(input, current_pos, directions):
    x,y = int(current_pos[0]), int(current_pos[1])
    # Get guard icon (^ > v <) of provided cordinates
    guard = input[y][x]
    # Create new cordinates to attempt to move to
    x_move, y_move = directions[guard]
    x_new, y_new = x+x_move, y+y_move
    # Replace guard from existing position with X
    input[y] = input[y][:x]+"X"+input[y][x+1:]
    # Ensure new position is not outside of grid. If so, finish
    if x_new >= 0 and y_new >= 0 and y_new < len(input):
        # Try moving to new location
        if input[y_new][x_new] == '#': # Turn Right
            # Get next guard icon from dict. They are in order of turning right
            direction_index = [*directions].index(guard)+1
            direction_index = 0 if direction_index >= len(directions) else direction_index
            new_guard_direction = list(directions)[direction_index]
            # Obtain turning cordinates of new guard icon and apply to X & Y
            x_turn, y_turn = directions[new_guard_direction]
            x_new, y_new = x+x_turn, y+y_turn
            # Add guard icon in new position
            input[y_new] = input[y_new][:x_new]+new_guard_direction+input[y_new][x_new+1:]
        else: # Proceed straight & add guard icon in new position
            input[y_new] = input[y_new][:x_new]+guard+input[y_new][x_new+1:]
        # Try to move again with new grid 
        move(input, (x_new,y_new), directions)
    else:
        print("\nFinal Grid:")
        for i in input:
            print(i)
        count_hash = sum([i.count('X') for i in input])
        print("Part A answer:", count_hash) # 5080



start = find_start(grid)
print("start cordinates:", start)

move(grid, start, directions)
