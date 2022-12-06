def find_marker(signal, count):
    for k in range(len(signal) - count):
        a = signal[k:k + count]
        unique_chars = set()
        for char in a:
            unique_chars.add(char)
        if len(unique_chars) == count:
            return k + count


# Read in input
file = open("input.txt", "r")
chars = file.read()

p1 = find_marker(chars, 4)
p2 = find_marker(chars, 14)

f = open("output.txt", "w")
f.write(f'Part 1: {p1}\n')
f.write(f'Part 2: {p2}')
