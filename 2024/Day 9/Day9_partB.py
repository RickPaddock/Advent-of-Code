### Massively inefficient but gets there in the end. I'll improve this later ###


with open('./input data/source_input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

nums = list(lines[0])

# Multiply index number by individual item(num) so it shows multiple times
# Had to do by range(1, int(num)+1) so double digits show as '11','11' and not '1111'
diskblock = []
groups = []
for n,num in enumerate(nums):
    for i in range(1, int(num)+1):
        num_multi = str((int(n)//2)) if (n+1)%2!=0 else "."
        if groups == [] or groups[-1] == num_multi:
            groups.append(num_multi)
        else:
            diskblock.append(groups)
            groups = [num_multi]

# append last group
if groups:
    diskblock.append(groups)

print(diskblock)

def move_last(input_list):
    new_list = []
    for count,back in enumerate(input_list[-1:0:-1]):
        print("count", count, back)
        if len(new_list) != 0:
            input_list = new_list
        new_list = []
        found = False
        if "." in back:
            continue
        else:
            for front_n, front in enumerate(input_list):
                space_diff = len(front) - len(back)
                if ("." not in front and front != back) or (front == back and found == False):
                    new_list.append(front)
                elif front == back and found == True:
                    new_list.append(["." for _ in range(len(back))])
                elif "." in front:
                    if found == True or space_diff < 0:
                        if "." in new_list[-1]:
                            new_list[-1].extend(front)
                        else:
                            new_list.append(front)
                    elif found == False and space_diff >= 0 and input_list.index(back) > input_list.index(front):
                        new_list.append(back)
                        if space_diff >0:
                            new_list.append(["." for _ in range(space_diff) if space_diff > 0])
                        found = True
                    else:
                        new_list.append(front)
        list_save = []
        for i in new_list:
            if len(list_save) == 0:
                list_save.append(i)
            else:
                if i[0] == "." and list_save[-1][0] == i[0]:
                    list_save[-1].extend(i)
                else:
                    list_save.append(i)
        new_list = list_save
    return list_save




diskblock_moved = move_last(diskblock)
print(diskblock_moved)

number = ''
for i in diskblock_moved:
    for num in i:
        num = str(0) if num == "." else num
        number += num

print(number)
print("Answer B:", sum([i*int(num) for i,num in enumerate(number)]))