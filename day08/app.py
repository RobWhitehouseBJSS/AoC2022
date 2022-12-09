def tree_visible(grid, x, y):
    height = grid[x][y]
    visible = 4

    for i in range(0, x):
        if grid[i][y] >= height and not i == x:
            visible -= 1
            break

    for i in range(x, len(grid)):
        if grid[i][y] >= height and not i == x:
            visible -= 1
            break

    for i in range(0, y):
        if grid[x][i] >= height and not i == y:
            visible -= 1
            break

    for i in range(y, len(grid[x])):
        if grid[x][i] >= height and not i == y:
            visible -= 1
            break
    return visible


def tree_score(grid, x, y):
    height = grid[x][y]
    score = [0, 0, 0, 0]

    for i in range(x - 1, -1, -1):
        score[0] += 1
        if grid[i][y] >= height:
            break

    for i in range(x + 1, len(grid)):
        score[1] += 1
        if grid[i][y] >= height:
            break

    for i in range(y - 1, -1, -1):
        score[2] += 1
        if grid[x][i] >= height:
            break

    for i in range(y + 1, len(grid[x])):
        score[3] += 1
        if grid[x][i] >= height:
            break

    return score[0] * score[1] * score[2] * score[3]


file = open("input.txt", "r")
trees = [[tree for tree in grid.strip()] for grid in file]

p1 = 0
p2 = 0

for x_index, row in enumerate(trees):
    for y_index, column in enumerate(row):
        if tree_visible(trees, x_index, y_index) > 0:
            p1 += 1
        if tree_score(trees, x_index, y_index) > p2:
            p2 = tree_score(trees, x_index, y_index)

f = open("output.txt", "w")
f.write(f'Part 1: {p1}\n')
f.write(f'Part 2: {p2}')
