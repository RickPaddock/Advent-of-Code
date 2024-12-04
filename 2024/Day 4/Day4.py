with open('./input data/source_input.txt', 'r') as f:
    lines = f.readlines()

# clean strings (remove \n)
lines = [line.strip() for line in lines if line.strip()]

word = "XMAS"

word_find = 0
for ln, string in enumerate(lines):
    for cn, char in enumerate(string):
        if char == word[0]: # Only process if we find start of word ('X')
            for x,y in ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)):
                list_check = ln
                char_check = cn
                sum_letters = 1
                # Loop remaining letters and count number that match the word in the direction
                for word_pos in range(len(word)-1):
                    list_check += x
                    char_check += y
                    # Stay in the grid 
                    if (0 <= list_check < len(lines)) and (0 <= char_check < len(string)):  
                        if lines[list_check][char_check] == word[word_pos+1]:
                            sum_letters +=1
                            if sum_letters == len(word):
                                word_find +=1

print("ANSWER A:", word_find) # 2557


word_findB = 0
for ln, string in enumerate(lines):
    for cn, char in enumerate(string):
        # A is always the centre of the X
        if char == "A":
            # Stay in the grid 
            if (ln+1<len(lines)) and (ln-1 >= 0) and (cn+1<len(string)) and (cn-1 >= 0):  
                # Pull letters from all 4 corners of the X shape
                down_back = lines[ln+1][cn-1]
                down_fwd = lines[ln+1][cn+1] 
                up_fwd = lines[ln-1][cn+1]
                up_back = lines[ln-1][cn-1]
                if  (
                        (
                            (down_back == "S" and up_fwd == "M") or
                            (down_back == "M" and up_fwd == "S")
                        ) 
                        and
                        (
                            (down_fwd == "M" and up_back == "S") or
                            (down_fwd == "S" and up_back == "M")
                        ) 
                    ):
                    word_findB += 1


print("ANSWER B:", word_findB) # 1854