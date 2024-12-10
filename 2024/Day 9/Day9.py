with open('./input data/source_input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

nums = list(lines[0])

# Multiply index number by individual item(num) so it shows multiple times
# Had to do by range(1, int(num)+1) so double digits show as '11','11' and not '1111'
diskblock = []
for n,num in enumerate(nums):
    for i in range(1, int(num)+1):
        num_multi = str((int(n)//2)) if (n+1)%2!=0 else "."
        diskblock.append(num_multi)

# All index locations of "."
def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)

spaces_lst = indices(diskblock, ".")

no_missing = [i for i in diskblock if i != "."]

# Move last item to next "." index position. 
# More efficient using index position than loop of large no_missing list
for inx in spaces_lst:
    no_missing.insert(inx,no_missing[-1])
    no_missing.pop()

print("Answer A:", sum([i*int(num) for i,num in enumerate(no_missing)]))