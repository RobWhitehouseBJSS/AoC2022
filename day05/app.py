from copy import deepcopy


def generate_crates(input):
    col_count = int(input.split("\n")[-1][-1])
    output = [[] * col_count for _ in range(col_count)]
    for line in input.split("\n"):
        column = 0
        for x in line[1::4]:
            if x.isalpha():
                output[column].append(x)
            column += 1
    for column in output:
        column.reverse()
    return output


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
raw_columns, moves = file.read().split("\n\n")

crates = generate_crates(raw_columns)
moves = [[int(x) for x in line.split() if x.isdigit()] for line in moves.splitlines()]

p1 = part1(deepcopy(crates), moves)
p2 = part2(deepcopy(crates), moves)

f = open("output.txt", "w")
f.write(f'Part 1: {p1}\n')
f.write(f'Part 2: {p2}')
