from typing import Literal
from functools import cmp_to_key

# Rules is a dict[PageNumber1, dict[PageNumber2, Ordering]]
type Ordering = Literal["reversed", "as-is"]
type Rules = dict[int, dict[int, Ordering]]

def parse_rules(text: str) -> Rules: 
    rules: Rules = {}
    for line in text.splitlines():
        a, b = map(int, line.split("|"))

        if a not in rules:
            rules[a] = {}
        if b not in rules:
            rules[b] = {}

        rules[a][b] = "as-is"
        # if a in rules[b]:
        #     print("Wtf")
        rules[b][a] = "reversed"

    return rules

def parse_int_list(text: str) -> list[int]:
    return [int(num) for num in text.split(",")]

rules, orders = open("./input.txt").read().split("\n\n")
rules: Rules = parse_rules(rules)
orders = [parse_int_list(line) for line in orders.splitlines()]
result = 0

def compare(a: int, b: int) -> int:
    global rules
    if a not in rules or b not in rules:
        return 0
    if rules[a][b] == "as-is":
        return -1
    else:
        return 1

# time complexity per order is O(n^2 * lookuptime)
#   n is input lenght
#   dict look up time is (~)constant anyway\
for order in orders:
    for i, num in enumerate(order):
        appliable_rules = rules[num].keys()
        for j in range(i + 1, len(order)):
            if order[j] not in appliable_rules:
                continue
            if rules[num][order[j]] == "reversed":
                break
        else:
            continue
        break
    else:
        continue
    # sort it
    sorted_order = sorted(order, key=cmp_to_key(compare))
    print(sorted_order)
    result += sorted_order[len(order)//2]


# print(len(orders))
print(result)


