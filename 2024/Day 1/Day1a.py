import requests

# Source text file
#text_file = "source_input_test.txt"
text_file = "source_input.txt"
source_data_loc = f"https://raw.githubusercontent.com/RickPaddock/Advent-of-Code/refs/heads/main/2024/Day 1/input data/{text_file}"

# Read text file
response = requests.get(source_data_loc)

if response.status_code == 200:
    content = response.text
    lines = content.splitlines()
    print("Source data (1st 10 rows):", lines[:10])
else:
    raise Exception(f"Failed to fetch file. Status code: {response.status_code}")

# Insert lines of numbers into to 2 seperate lists & ascending sort 
left_list = []
right_list = []
for line in lines:
    col1, col2 = map(int, line.split())
    left_list.append(col1)
    right_list.append(col2)

left_list.sort()
right_list.sort()

# Zip so 1st values from each list are together, then 2nd, and so on
lists_zipped= list(zip(left_list, right_list))

sum_items = sum([abs(i[0] - i[1]) for i in lists_zipped])

print("Answer:", sum_items)
