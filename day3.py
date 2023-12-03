f = open("day3.txt", "r")
grid = []

for x in f:
    line = x.strip()
    grid.append(line)

def check_valid(r, c):
    if not grid[r][c].isdigit() and grid[r][c] != ".":
        return True
    return False

def handle_add(r, c):
    num = 0
    end_c = c
    while end_c < len(grid[r]) and grid[r][end_c].isdigit():
        num *= 10
        num += int(grid[r][end_c])
        end_c += 1
    end_c -= 1
    if r > 0:
        for i in range(max(0, c-1), min(len(grid[r]), end_c+2)):
            if check_valid(r-1, i):
                return end_c, num
    if r < len(grid)-1:
        for i in range(max(0, c-1), min(len(grid[r]), end_c+2)):
            if check_valid(r+1, i):
                return end_c, num
    if c > 0:
        if check_valid(r, c-1):
            return end_c, num
    if end_c < len(grid[r])-1:
        if check_valid(r, end_c+1):
            return end_c, num
    return end_c, 0

star_dict = {}

def check_star(r, c, num):
    if grid[r][c] == "*":
        if (r, c) in star_dict:
            return True, star_dict[(r, c)]*num
        else:
            star_dict[(r, c)] = num
            return True, 0
    return False, 0

def handle_gear(r, c):
    num = 0
    end_c = c
    while end_c < len(grid[r]) and grid[r][end_c].isdigit():
        num *= 10
        num += int(grid[r][end_c])
        end_c += 1
    end_c -= 1
    total = 0
    if r > 0:
        for i in range(max(0, c-1), min(len(grid[r]), end_c+2)):
            star, ret = check_star(r-1, i, num)
            if star:
                total += ret
    if r < len(grid)-1:
        for i in range(max(0, c-1), min(len(grid[r]), end_c+2)):
            star, ret = check_star(r+1, i, num)
            if star:
                total += ret
    if c > 0:
        star, ret = check_star(r, c-1, num)
        if star:
            total += ret
    if end_c < len(grid[r])-1:
        star, ret = check_star(r, end_c+1, num)
        if star:
            total += ret
    return end_c, total
        

def part1():
    total = 0
    for r in range(len(grid)):
        c = 0
        while c < len(grid[r]):
            if grid[r][c].isdigit():
                c, num = handle_add(r, c)
                total += num
            c += 1
    print(total)

def part2():
    total = 0
    for r in range(len(grid)):
        c = 0
        while c < len(grid[r]):
            if grid[r][c].isdigit():
                c, num = handle_gear(r, c)
                total += num
            c += 1
    print(total)

if __name__ == '__main__':
    part1()
    part2()