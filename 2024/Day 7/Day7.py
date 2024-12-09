from itertools import product

with open('./input data/source_input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

print(lines)

# Split answer and nums, then again into seperate lists
cleaned = [[x.strip() for x in i.split(":")] for i in lines]
cleaned = [[i[0],i[1].split(' ')] for i in cleaned]
print(cleaned)

#Part A
operators = ["+","*"]
#Part B
#operators = ["|","+","*"]


def generate_combinations(operators, level):
    """ Get all combinations of operators per number of spaces between number list """
    return list(product(operators, repeat=level))

# Capture all combinations up to max so we only have to call function once per level
max_spaces = 0
for item in cleaned:
    num_spaces = len(item[1]) - 1  # Spaces are one less than the number of elements
    max_spaces = max(max_spaces, num_spaces)

print("MAX SPACES:", max_spaces)
all_combos = {}
for n in range(1,max_spaces+1):
    all_combos[n] = generate_combinations(operators, n)


### Pretty slow so I'm sure there are more efficient ways. Better than using ZIP & EVAL though ###
collect = []
for n, values in enumerate(cleaned):
    answer = int(values[0])  # The expected answer
    nums = values[1]  # List of numbers
    spaces = len(nums) - 1  # Number of spaces (operations)
    combos = all_combos[spaces]  # Get the possible operations
    
    print(n, ".....", nums)

    # Process the possible combinations of operators for the given numbers
    for math in combos:
        result = nums[0]  
        for i, op in enumerate(math):  # Loop over the operators and apply to the numbers
            num = nums[i + 1]  
            if op == "|":
                result = str(result) + str(num)  # Concatenate if operator is "|"
            elif op == "+":
                result = int(result) + int(num)  # Perform addition
            elif op == "*":
                result = int(result) * int(num)  # Perform multiplication

        # Check if the result matches the expected answer
        if int(result) == answer:
            collect.append(int(result))
            break  # No need to check other combinations, move to the next entry in `cleaned`

print("Collected results:", collect)
print("Sum of results:", sum(collect))
