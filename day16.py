import queue

# lol.
def step(r, c, dir, grid, q):
    if grid[r][c] == "|":
        if dir == "r" or dir == "l":
            q.put([r-1, c, "u"])
            q.put([r+1, c, "d"])
        else:
            if dir == "d":
                q.put([r+1, c, "d"])
            else:
                q.put([r-1, c, "u"])
    elif grid[r][c] == "-":
        if dir == "u" or dir == "d":
            q.put([r, c-1, "l"])
            q.put([r, c+1, "r"])
        else:
            if dir == "l":
                q.put([r, c-1, "l"])
            else:
                q.put([r, c+1, "r"])
    elif grid[r][c] == "/":
        if dir == "l":
            q.put([r+1, c, "d"])
        elif dir == "r":
            q.put([r-1, c, "u"])
        elif dir == "d":
            q.put([r, c-1, "l"])
        else:
            q.put([r, c+1, "r"])
    elif grid[r][c] == "\\":
        if dir == "l":
            q.put([r-1, c, "u"])
        elif dir == "r":
            q.put([r+1, c, "d"])
        elif dir == "u":
            q.put([r, c-1, "l"])
        elif dir == "d":
            q.put([r, c+1, "r"])
    else:
        if dir == "l":
            q.put([r, c-1, "l"])
        elif dir == "r":
            q.put([r, c+1, "r"])
        elif dir == "d":
            q.put([r+1, c, "d"])
        elif dir == "u":
            q.put([r-1, c, "u"])

def run_search(r, c, dir, grid):
    energized = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    seen = set()
    q = queue.Queue()
    q.put([r, c, dir])
    while not q.empty():
        r, c, dir = q.get()
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r, c, dir) in seen:
            continue
        energized[r][c] = 1
        seen.add((r, c, dir))
        step(r, c, dir, grid, q)
        
    total = 0
    for r in range(len(energized)):
        for c in range(len(energized[r])):
            if energized[r][c] == 1:
                total += 1
    return total

def part1():
    with open('inputs/day16.txt', 'r') as f:
        grid = [x.strip() for x in f]
        return run_search(0, 0, 'r', grid)
    
def part2():
    with open('inputs/day16.txt', 'r') as f:
        grid = [x.strip() for x in f]

        maximum = 0
        # Run all horizontal entry points
        for r in range(len(grid)):
            res = run_search(r, 0, 'r', grid)
            if res > maximum:
                maximum = res
            res = run_search(r, len(grid[r])-1, 'l', grid)
            if res > maximum:
                maximum = res

        # Run all vertical entry points
        for c in range(len(grid)):
            res = run_search(0, c, 'd', grid)
            if res > maximum:
                maximum = res
            res = run_search(len(grid)-1, c, 'u', grid)
        return maximum

if __name__ == '__main__':
   print(part1())
   print(part2())