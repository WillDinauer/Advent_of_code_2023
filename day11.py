def day11(num):
    f = open('inputs/day11.txt', 'r')

    galaxies = []
    grid = []

    for x in f:
        grid.append(x.strip())
    
    empty_c, empty_r = [], []
    for c in range(len(grid[0])):
        is_empty = True
        for r in range(len(grid)):
            if grid[r][c] == "#":
                is_empty=False
        if is_empty:
            empty_c.append(c)
    
    for r in range(len(grid)):
        is_empty = True
        for c in range(len(grid[r])):
            if grid[r][c] == "#":
                is_empty = False
        if is_empty:
            empty_r.append(r)
    
    added_r = 0
    for r in range(len(grid)):
        added_c = 0
        if r in empty_r:
            added_r += num
        for c in range(len(grid[r])):
            if c in empty_c:
                added_c += num
            if grid[r][c] == "#":
                galaxies.append([r+added_r, c+added_c])
    total = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            total += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1]-galaxies[j][1])
    return total

def part1():
    return day11(1)

def part2():
    return day11(999999)

if __name__ == '__main__':
    print(part1())
    print(part2())