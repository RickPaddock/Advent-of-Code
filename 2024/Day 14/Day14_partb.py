import math

##TO DO#################################################################################
# Need to change this for part B to calculate all robot positions after each iteration #
# Currently it does all moves for one robot at a time                                  #
########################################################################################

test = False
if test:
    file = "source_input_test.txt"
    tall = 7
    wide = 11
else:
    file = "source_input.txt"
    tall = 103
    wide = 101

# create lobby
lobby = [(x,y) for y in range(tall) for x in range(wide)]
#print(lobby)


def quadrants(tall, wide, lobby):
    quad_wide = wide // 2
    quad_tall = tall // 2
    top_left, top_right, bottom_left, bottom_right = [], [], [], []
    for l in lobby:
        x,y = l[0],l[1]
        if x < quad_wide and y < quad_tall:
            top_left.append((x,y))
        elif x > quad_wide and y < quad_tall:
            top_right.append((x,y))
        elif x < quad_wide and y > quad_tall:
            bottom_left.append((x,y))
        elif x > quad_wide and y > quad_tall:
            bottom_right.append((x,y))
    return (top_left, top_right, bottom_left, bottom_right)

four_quadrants = quadrants(tall, wide, lobby)


with open(f"./input data/{file}", 'r') as f:
    robots = [line.strip() for line in f.readlines()]

#print(robots)

# Extract robot starting positions & velocity
def robot_starting(robot):
    start_x = int(robot[robot.find("p=")+2:robot.find(",")].strip())
    start_y = int(robot[robot.find(",")+1:robot.find("v")].strip())
    return (start_x, start_y)


def robot_velocity(robot):
    v_start = robot.find("v=")
    vel_x = robot[v_start+2:robot.find(",",v_start)].strip()
    vel_y = robot[robot.find(",",v_start)+1:].strip()
    return (vel_x, vel_y)


def move_robot(tall, wide, start_xy, vel_xy, iterations):
    move_to_x = (int(start_xy[0]) + (int(vel_xy[0]) * iterations)) % wide
    move_to_y = (int(start_xy[1]) + (int(vel_xy[1]) * iterations)) % tall
    final_xy = (move_to_x, move_to_y)
    return final_xy


all_robots = []
for robot in robots:
    robot_start_xy = robot_starting(robot)
    robot_vel_xy = robot_velocity(robot)
    robot_moved = move_robot(tall, wide, robot_start_xy, robot_vel_xy, 100)
    all_robots.append(robot_moved)
print(f"all_robots: {all_robots}")


def count_robot_per_quad(all_robots, four_quadrants):
    quadrant_count = []
    for quad in four_quadrants: # Loop 4 quads
        cumulative_count = 0
        for robot in all_robots:
            cumulative_count += 1 if robot in quad else 0
        quadrant_count.append(cumulative_count)
    return quadrant_count

print("PART A:",math.prod(count_robot_per_quad(all_robots, four_quadrants)))


## PART B ##
# I noticed there was a pattern forming every 101 moved starting at position 22 
with open(f"./input data/find_tree.txt", 'w') as f:
    for moves in range(22, 10000, 101):  
        print(f"Iteration {moves}", file=f)
        all_robots = []
        for robot in robots:
            robot_start_xy = robot_starting(robot)
            robot_vel_xy = robot_velocity(robot)
            robot_moved = move_robot(tall, wide, robot_start_xy, robot_vel_xy, moves)
            all_robots.append(robot_moved)
        for y in range(tall):
            row = ""
            for x in range(wide):
                row += '#' if (x, y) in all_robots else ' '
            print(row, file=f)

# Tree found at 6587
