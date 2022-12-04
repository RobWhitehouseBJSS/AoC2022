def get_value(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


file = open("input.txt", "r")
bags = [bag.strip() for bag in file.readlines()]

p1_total = 0
p2_total = 0

for bag in bags:
    half = len(bag) // 2
    right, left = bag[:half], bag[half:]
    common = set(left).intersection(set(right))
    p1_total += get_value(common.pop())

for x in range(0, len(bags), 3):
    common = set(bags[x]).intersection(bags[x+1]).intersection(bags[x+2])
    p2_total += get_value(common.pop())

f = open("output.txt", "w")
f.write(f'Part 1: {p1_total}\n')
f.write(f'Part 2: {p2_total}')
