with open('./input data/source_input.txt', 'r') as f:
    stones = [line.strip() for line in f.readlines()]

stones = [int(x) for x in stones[0].split()]

def calc_number(num: int):
    num_len = len(str(abs(num)))
    if num == 0:
        return [1]
    elif num_len >1 and num_len%2==0:
        return [int(str(num)[0:int(num_len/2)]) , int(str(num)[int(num_len/2):])]
    else:
        return [num*2024]


def stones_iterations(stones, loop):
    """ Return counter dict for integers calculated by calc_number function """
    # An int can only have one outcome. Save and reuse rather than recalculate
    memory_calc = {} 
    # Set counter to 1 for current stones
    stone_counts = {stone: 1 for stone in stones}
    for i in range(loop): 
        #print(f"LOOP: {i+1}") 
        new_stone_counts = {}
        for stone, count in stone_counts.items(): # uses previous loop output as input
            if stone not in memory_calc:
                memory_calc[stone] = calc_number(stone) # Reuse calculations
            birth_stones = memory_calc[stone]
            for new_stone in birth_stones:
                if new_stone not in new_stone_counts: # Initiate entry for new stones
                    new_stone_counts[new_stone] = 0
                new_stone_counts[new_stone] += count # Record multiple stones in one itteration
        stone_counts = new_stone_counts # Only take latest stones to next round
    return stone_counts


partA = stones_iterations(stones,25)
print("Answer A:", sum(partA.values()))

partB = stones_iterations(stones, 75)
print("Answer B:", sum(partB.values()))

