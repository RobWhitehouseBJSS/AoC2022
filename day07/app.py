# Read in input
file = open("input.txt", "r")
commands = file.readlines()

root = {".name": "/", ".type": "d"}
current = None
path = []

for command in commands:
    command = command.split()
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == "/":
                current = root
            elif command[2] == "..":
                current = path.pop()
            else:
                path.append(current)
                current = current[command[2]]
    elif command[0] == "dir":
        current[command[1]] = {".name": command[1], ".type": "d"}
    else:
        current[command[1]] = {".name": command[1], ".type": "f", ".size": int(command[0])}


def get_size(n):
    if n[".type"] == "f":
        return n[".size"]
    return sum(get_size(v) for k, v in n.items() if not k.startswith("."))


def create_size_list(current, size_list):
    size_list.append(get_size(current))
    for k, v in current.items():
        if not k.startswith(".") and v[".type"] == "d":
            create_size_list(v, size_list)

def part_2(size_list):
    free_space = 70000000 - size_list[0]
    for dir in sorted(size_list):
        if free_space + dir >= 30000000:
            return dir


size_list = []
create_size_list(root, size_list)
p1 = sum([s for s in size_list if s < 100_000])
p2 = part_2(size_list)

f = open("output.txt", "w")
f.write(f'Part 1: {p1}\n')
f.write(f'Part 2: {p2}')
