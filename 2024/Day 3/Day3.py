
import re

with open('./2024/Day 3/input data/Day3.txt', 'r') as f:
    lines = f.readlines()

# Pull all lines together as one
all_lines = " ".join(line.strip() for line in lines)

def multiplied_numbers(input_str):
    # Pattern match 'mul(1to3 digits,1to3 digits)'. Only return the digits and ','
    multiply_lst = re.findall("(?<=mul\()\d{1,3}\,\d{1,3}(?=\))", input_str)

    # Split digits by "," and multiply together
    return [int(num[0]) * int(num[1]) for num in (num.split(",") for num in multiply_lst)]

print("Part A answer:", sum(multiplied_numbers(all_lines))) # 178794710

# Split list by 'do' & removed those starting n't (i.e. don't). Put back together as string
do_lines = "".join(i for i in all_lines.split("do") if i[0:3] != "n't")

print("Part B answer:", sum(multiplied_numbers(do_lines))) # 178794710
