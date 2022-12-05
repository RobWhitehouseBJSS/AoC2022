file = open("input.txt", "r")
jobs = [[[int(i) for i in assignment.split("-")] for assignment in job.strip().split(',')] for job in file.readlines()]

p1 = 0
p2 = 0

for (a, b), (c, d) in jobs:
    if a <= c <= d <= b or c <= a <= b <= d:
        p1 += 1
    if a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d:
        p2 += 1

f = open("output.txt", "w")
f.write(f'Part 1: {p1}\n')
f.write(f'Part 2: {p2}')
