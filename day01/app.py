# Read in input
file = open("input.txt", "r")
lines = file.readlines()

totals = []
elf_total = 0

for line in lines:
    line = line.strip('\n')
    if line != "":
        elf_total += int(line)
    else:
        totals.append(elf_total)
        elf_total = 0

totals.sort(reverse=True)
part2_total = totals[0] + totals[1] + totals[2]

f = open("output.txt", "w")
f.write(f'Part 1: {totals[0]}\n')
f.write(f'Part 2: {part2_total}\n')
