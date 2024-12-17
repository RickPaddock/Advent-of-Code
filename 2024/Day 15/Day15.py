
# Still have to do Part B and tidy this up

with open(f"./input data/source_input_test.txt", 'r') as f:
    input = [line.strip() for line in f.readlines() if line.strip()]


grid = [x for x in input if x[0] == '#']
# Part B .... Double Grid
grid = [''.join(i*2 for i in x) for x in grid]
# Only want 1 @ though so replace 2nd @ with '.'
for y, str in enumerate(grid):
    for x, val in enumerate(str):
        if val == "@" and grid[y][x-1] == "@":
            grid[y] = grid[y][:x] +"."+grid[y][x+1:]


for g in grid:
    print(g)

all_walls = [(n_x,n_y) for n_y,y in enumerate(grid) for n_x,x in enumerate(y) if x == '#']
print("all_walls", all_walls)

all_boxes = [(n_x,n_y) for n_y,y in enumerate(grid) for n_x,x in enumerate(y) if x == 'O']
print("all_boxes", all_boxes)


moves = [char for i in input for char in i if char in ('<','^','>','v')]
print(moves)


# -2 considers # borders
area_y = len(grid)-2
area_x = len(grid[0])-2


directions = {"^": (0,-1),">":(1,0),"v":(0,1),"<":(-1,0)}


def find_start(input, robot):
    for y, str in enumerate(input):
        for x, val in enumerate(str):
            if val == robot:
                return x,y


def fwd_path(loc, facing, all_walls, all_boxes):
    x,y = loc[0], loc[1]
    while True:
        x_move, y_move = directions[facing]
        x_fwd,y_fwd = x+x_move,y+y_move
        if 1 <= y <= area_y and 1 <= x <= area_x:
            if (x_fwd,y_fwd) not in(all_walls) and (x_fwd,y_fwd) not in(all_boxes):
                return (x_fwd,y_fwd)
            elif (x_fwd,y_fwd) in(all_walls):
                return (None, None)
            x,y = x_fwd,y_fwd
        else:
            return (None, None)
        

current_loc = find_start(grid, '@')
print(f"start: {current_loc}")
for move in moves:
    #print("\nmove FROM" ,move, current_loc)
    #print("All boxes:", all_boxes)
    fwd_loc = fwd_path(current_loc, move, all_walls, all_boxes)
    #print("fdw loc:",fwd_loc)
    x_move, y_move = directions[move]
    if fwd_loc != (None,None): # Only perform move if there is space
        box_from_move = []
        box_to_move = []
        for box in all_boxes: # Add one to all boxes between current location and available space
            #print("BOX",current_loc[0],box[0],fwd_loc[0],"???",current_loc[1],box[1],fwd_loc[1])
            if (current_loc[0] <= box[0] <= fwd_loc[0] and current_loc[1] <= box[1] <= fwd_loc[1])\
                or\
                (current_loc[0] >= box[0] >= fwd_loc[0] and current_loc[1] >= box[1] >= fwd_loc[1]):
                #print("box FROM", box)
                box_from_move.append(box)
                box = (box[0]+x_move, box[1]+y_move)
                #print("box TO", box)
                box_to_move.append(box)
            #print("BOX MOVE", box_to_move)
        if len(box_to_move)>0: 
            #print("REMOVING", box_from_move,"from",all_boxes)
            all_boxes = [box for box in all_boxes if box not in box_from_move]
            #print("APPENDING", box_to_move,"TO",all_boxes)
            all_boxes.extend(box_to_move)
        current_loc = (current_loc[0]+directions[move][0], current_loc[1]+directions[move][1])
    #print("move TO" ,move, current_loc)


print("FINAL BOXES", all_boxes)
final = []
for box in all_boxes:
    final.append(100 * box[1] + box[0])
print(final)
print(sum(final))


