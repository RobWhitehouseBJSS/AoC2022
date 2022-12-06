from copy import deepcopy


def part1(crates, moves):
    for num, start, end in moves:
        for _ in range(num):
            crates[end - 1].append(crates[start - 1].pop())
    return "".join([x.pop() for x in crates])


def part2(crates, moves):
    for num, start, end in moves:
        crates[end - 1].extend(crates[start - 1][-num:])
        for _ in range(num):
            crates[start - 1].pop()
    return "".join([x.pop() for x in crates])


file = open("input.txt", "r")
unused, moves = file.read().split("\n\n")

moves = [[int(x) for x in line.split() if x.isdigit()] for line in moves.splitlines()]
crates = [
    ["D", "T", "R", "B", "J", "L", "W", "G"],
    ["S", "W", "C"],
    ["R", "Z", "T", "M"],
    ["D", "T", "C", "H", "S", "P", "V"],
    ["G", "P", "T", "L", "D", "Z"],
    ["F", "B", "R", "Z", "J", "Q", "C", "D"],
    ["S", "B", "D", "J", "M", "F", "T", "R"],
    ["L", "H", "R", "B", "T", "V", "M"],
    ["Q", "P", "D", "S", "V"]
]

p1 = part1(deepcopy(crates), moves)
p2 = part2(deepcopy(crates), moves)

f = open("output.txt", "w")
f.write(f'Part 1: {p1}\n')
f.write(f'Part 2: {p2}')
