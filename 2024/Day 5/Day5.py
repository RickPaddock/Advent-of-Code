with open('./input data/source_input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

rules = [val for val in lines if "|" in val]
pages = [val for val in lines if "," in val]
print(rules)
print(pages)


def is_good(page, rules) -> bool:
    """ Return False if values not in the same order as any matched rule, else return True """
    rule_result = True
    for rule in rules:
        try:
            pos1 = page.index(rule.split("|")[0])
            pos2 = page.index(rule.split("|")[1])
            if pos1 >= pos2: rule_result = False
        except:
            pass
    return rule_result


def get_middle(page) -> int:
    """ Split string into seperate list items and take the middle """
    page_lst = page.split(",")
    return int(page_lst[len(page_lst)//2])


# Append middle numbers only from pages which aren't rule breakers
good_middle = []
for page in pages:
    if is_good(page, rules):
        good_middle.append(get_middle(page))


print("Answer A:", sum(good_middle)) # 5129


# Part B
# Note: Quite inefficient and could be altered to continue the processing after a reorder rather than starting again
def reorder(page, rules) -> list:
    """ Reorder numbers to match the rule order if they are different """
    for i in range(len(page)-1):
        for rule1,rule2 in rules:
            # Only process those which are in the wrong order
            if page[i] == rule2 and page[i+1] == rule1:
                # Swap the numbers to match the rule
                page[i], page[i+1] = rule1, rule2
                # Start reorder process again with the newly ordered numbers
                page = reorder(page, rules)
    return page

# Append middle numbers only from pages which are rule breakers, after reordering 
bad_middle = []
for page in pages:
    if not is_good(page, rules):
        # Convert strings to lists for easier processing
        rules_split = [r.split("|") for r in rules]
        page_split = page.split(",")

        page_reordered = reorder(page_split, rules_split)

        # Convert list back to string
        page_reordered_str = ",".join(page_reordered)

        bad_middle.append(get_middle(page_reordered_str))


print("Answer B:", sum(bad_middle)) # 4077
