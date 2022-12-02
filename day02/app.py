scores_p1 = {"A X": 4, "A Y": 8, "B X": 1, "A Z": 3, "C X": 7, "B Y": 5, "B Z": 9, "C Y": 2, "C Z": 6}
scores_p2 = {"A Y": 4, "A Z": 8, "B X": 1, "A X": 3, "C Z": 7, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6}

# Read in input
file = open("input.txt", "r")
games = file.read().strip().splitlines()

p1_total = 0
p2_total = 0

for game in games:
    p1_total += scores_p1[game]
    p2_total += scores_p2[game]

f = open("output.txt", "w")
f.write(f'Part 1: {p1_total}\n')
f.write(f'Part 2: {p2_total}')