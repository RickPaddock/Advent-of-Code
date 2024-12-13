with open('./input data/source_input.txt', 'r') as f:
    claw = [line.strip() for line in f.readlines()]

#print(claw)

# Thought id try named tuples. Could do it without
from collections import namedtuple
Game = namedtuple("Game", ["button_a", "button_b", "prize"])

# Pull X & Y from row. For buttons A&B and Prize
def extract_game_details(game):
    x = game[game.find("X")+2:game.find(",")].strip()
    y = game[game.find("Y")+2:].strip()
    return (int(x),int(y))


# Extract (x,y) from button A/B/Prize & insert into named tuple
games_namedtuple = []
games = []    
current_game = []
for game in claw:
    if game: # Don't read in spaces
        current_game.append(extract_game_details(game))
    if len(current_game) == 3: # Capture every 3rd so a game has 2 buttons and a prize
        games_namedtuple.append(Game(current_game[0], current_game[1], current_game[2]))
        current_game = []


# Had to look up "Cramer's Rule" to get this solution. Never would have worked it out alone!
def calculate(game):
    """ Calculate most efficienct button presses with costs A+3 and B+1 per press """
    det = game.button_a[0] *  game.button_b[1] -  game.button_a[1] *  game.button_b[0]
    # [0] = X & [1] = Y
    a = (game.prize[0] * game.button_b[1] - game.prize[1] * game.button_b[0]) / det
    b = (game.button_a[0] * game.prize[1] - game.button_a[1] * game.prize[0]) / det
    total_cost = (int(a) * 3) + (int(b) * 1)
    # Only return those which can be solved. is_integer() checks for whole numbers
    if a.is_integer() and b.is_integer():
        return total_cost
    else:
        return 0

## PART A ##
solvable_games = []
for game in games_namedtuple:
    total_cost = calculate(game)
    solvable_games.append(total_cost)
print("PART A:", sum(solvable_games))

## PART B ##
solvable_games = []
for game in games_namedtuple:
    new_prize = (game.prize[0] + 10000000000000, game.prize[1] + 10000000000000)
    game = game._replace(prize=new_prize) # _replace returns new tuple
    total_cost = calculate(game)
    solvable_games.append(total_cost)
print("PART B:", sum(solvable_games))