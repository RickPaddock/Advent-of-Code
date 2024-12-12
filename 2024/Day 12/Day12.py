with open('./input data/source_input.txt', 'r') as f:
    garden = [line.strip() for line in f.readlines()]


MAX_X = len(garden[0]) 
MAX_Y = len(garden)


# up,down,left,right
directions = [(0,-1),(0,1),(-1,0),(1,0)]


def is_in_garden(loc):
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


# for i in garden:
#     print(i)


def find_plot_sizes(garden, start):
    """ Find all garden plots and perimiter count of each """
    # Only proceed with logic if start location hasn't already been assigned to a plot
    if all(start not in plot for plot in success_plots):
        current_plot = set([start])
        stack = [(start)]
        # Stack will be populated when new values for the current plot are found and processed
        while stack:
            (x, y) = stack.pop()
            # plot starts with 4 perimiters until matching plots are touching
            if (x, y) not in perim_dict:
                perim_dict[(x, y)] = 4
            # Explore all possible moves from current position
            for direction_xy in look_around((x, y)):
                if is_in_garden(direction_xy) and all(direction_xy not in plot for plot in success_plots):
                    current_plot_val = (garden[y][x])
                    looking_plot_val = (garden[direction_xy[1]][direction_xy[0]])
                    if looking_plot_val == current_plot_val:
                        perim_dict[(x,y)] -=1
                        if direction_xy not in current_plot:
                            # Plot is of same value so append to stack to check later
                            stack.append((direction_xy))
                            current_plot.add((direction_xy))
        success_plots.append(current_plot)


success_plots = []
perim_dict = {}
# Loop the entire garden and use each individual location as a start point
for y,y_val in enumerate(garden):
    for x in range(len(y_val)):
        print("\nStart",x,y)
        find_plot_sizes(garden,(x,y))


print("PART A:",sum([len(plot)*sum([perim_dict[i] for i in plot]) for plot in success_plots]))


# PART B - Now interested in whole fence, not just the singular perimiters
# For all plots, scan via the Y-axis to put top/bottom fences, then X for left/right
cumulative = 0
for plot in success_plots:
    fence = 0
    # >> Scan along all Y-axis in the current plot <<
    Y = set([x_y[1] for x_y in plot])
    for y_loop in Y:
        # For efficiency only look at relavent X-axis which are in current plot
        x_min = min([x_y[0] for x_y in plot])
        x_max = max([x_y[0] for x_y in plot])
        for x in range(x_min, x_max+1):
            if (x, y_loop) in plot:
                # check up
                if (x, y_loop-1) not in plot and ((x+1, y_loop) not in plot or (x+1, y_loop-1) in plot):
                    fence += 1
                # check down
                if (x, y_loop+1) not in plot and ((x+1, y_loop) not in plot or (x+1, y_loop+1) in plot):
                    fence += 1
    # >> Scan along all X-axis in the current plot <<
    X = set([x_y[0] for x_y in plot])
    for x_loop in X:
        # For efficiency only look at relavent Y-axis which are in current plot
        y_min = min([x_y[1] for x_y in plot])
        y_max = max([x_y[1] for x_y in plot])
        for y in range(y_min, y_max+1):
            if (x_loop, y) in plot:
                # check left 
                if (x_loop-1, y) not in plot and ((x_loop, y+1) not in plot or (x_loop-1, y+1) in plot):
                    fence += 1
                # check right
                if (x_loop+1, y) not in plot and ((x_loop, y+1) not in plot or (x_loop+1, y+1) in plot):
                    fence += 1

    total = len(plot)*fence
    cumulative += total

print(f"PART B: {cumulative}")
