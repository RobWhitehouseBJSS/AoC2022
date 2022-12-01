# Read in input
file = open("input.txt", "r")
elves = file.read().strip().split('\n\n')

totals = []
elf_total = 0

for elf in elves:
    totals.append(sum(map(int, elf.split('\n'))))

f = open("output.txt", "w")
f.write(f'Part 1: {max(totals)}\n')
f.write(f'Part 2: {sum(sorted(totals)[-3:])}\n')
