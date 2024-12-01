import requests

# Source text file: 2 columns of numbers
#text_file = "Day1_test.txt"
text_file = "Day1.txt"
source_data_loc = f"https://raw.githubusercontent.com/RickPaddock/Advent-of-Code/refs/heads/main/2024/Day 1/input data/{text_file}"

# Read text file
response = requests.get(source_data_loc)

if response.status_code == 200:
    content = response.text
    lines = content.splitlines()
    print("Source data (1st 10 rows):", lines[:10])
else:
    raise Exception(f"Failed to fetch file. Status code: {response.status_code}")

# Insert lines of numbers into to 2 seperate lists
left_list = []
right_list = []
for line in lines:
    col1, col2 = map(int, line.split())
    left_list.append(col1)
    right_list.append(col2)

# Unique dictionary of items in left_list to capture the num of occurances in right_list
left_list_items = dict.fromkeys(sorted(set(left_list)))

# For all unique left_list items, count occurances in right_list, & add back to dict
for i in left_list_items.keys():
    count = 0
    for x in right_list:
        if i == x:
            count += 1 
    left_list_items[i] = count

# Loop left_list and multiple by occurances in right_list
multiply_items = sum([i * left_list_items[i] for i in left_list])
    
print("Answer:", multiply_items)
