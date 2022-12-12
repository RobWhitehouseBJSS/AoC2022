def update_pixels(x, cycles, pixels):
    pos = (cycles - 1) % 40
    if pos in {x - 1, x, x + 1}:
        pixels[cycles - 1] = "#"


file = open("input.txt", "r")
lines = [[line for line in line.strip("\n").split(" ")] for line in file]

x = 1
cycles = 0
signal_strengths = {}
pixels = list("." * 40 * 6)

for line in lines:
    if line[0] == 'addx':
        cycles += 1
        signal_strengths[cycles] = x * cycles
        update_pixels(x, cycles, pixels)
        cycles += 1
        signal_strengths[cycles] = x * cycles
        update_pixels(x, cycles, pixels)
        x += int(line[1])
    elif line[0] == 'noop':
        cycles += 1
        signal_strengths[cycles] = x * cycles
        update_pixels(x, cycles, pixels)

p1 = sum(signal_strengths.get(i, 0) for i in range(20, 221, 40))

f = open("output.txt", "w")
f.write(f'Part 1: {p1}\n')
for i in range(0, 201, 40):
    print("".join(pixels[i: i + 40]))
