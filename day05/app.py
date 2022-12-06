file = open("input.txt", "r")
crates, moves = file.read().split("\n\n")

moves = [[int(x) for x in line.split() if x.isdigit()] for line in moves.splitlines()]
crates = []

for num, start, end in moves:
    for i in range(num):
        crates[end - 1].apphend(crates[start - 1].pop())

p1 = "".join([x.pop() for x in crates])

f = open("output.txt", "w")
f.write(f'Part 1: {p1}\n')
# f.write(f'Part 2: {p2}')

