import queue

def part1():
    f = open('inputs/day10.txt', 'r')

    grid = []
    for x in f:
        grid.append(x.strip())
    
    s_r, s_c = 0, 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "S":
                s_r = r
                s_c = c
                break
    
    seen = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    seen[s_r][s_c] = 1

    directions = {"|": ["u", "d"], "-": ["l", "r"], "L": ["u", "r"], "J": ["u", "l"], "7": ["l", "d"], "F": ["r", "d"], ".": [], "S": []}
    coming_from = {"|": ["u", "d"], "-": ["l", "r"], "L": ["d", "l"], "J": ["d", "r"], "7": ["r", "u"], "F": ["l", "u"], ".": [], "S": []}

    def connected(character, direction):
        if direction in coming_from[character]:
            return True, directions[character]
        return False, "e"

    q = queue.Queue()
    q.put([s_r+1, s_c, "d", 2])
    q.put([s_r-1, s_c, "u", 2])
    q.put([s_r, s_c+1, "r", 2])
    q.put([s_r, s_c-1, "l", 2])

    best_step = 0
    while not q.empty():
        r, c, dir, step = q.get()
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            continue

        connects, next_dirs = connected(grid[r][c], dir)
        if connects and seen[r][c] == 0:
            seen[r][c] = step
            if step > best_step:
                best_step = step

            for next_dir in next_dirs:
                if next_dir == "l":
                    q.put([r, c-1, "l", step+1])
                elif next_dir == "r":
                    q.put([r, c+1, "r", step+1])
                elif next_dir == "u":
                    q.put([r-1, c, "u", step+1])
                elif next_dir == "d":
                    q.put([r+1, c, "d", step+1])
    return best_step

# This isn't great.
def part2():
    f = open('inputs/day10.txt', 'r')

    grid = []
    for x in f:
        grid.append(x.strip())
    
    s_r, s_c = 0, 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "S":
                s_r = r
                s_c = c
                break
    
    seen = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
    seen[s_r][s_c] = 0

    directions = {"|": ["u", "d"], "-": ["l", "r"], "L": ["u", "r"], "J": ["u", "l"], "7": ["l", "d"], "F": ["r", "d"], ".": [], "S": []}
    coming_from = {"|": ["u", "d"], "-": ["l", "r"], "L": ["d", "l"], "J": ["d", "r"], "7": ["r", "u"], "F": ["l", "u"], ".": [], "S": []}

    def connected(character, direction):
        if direction in coming_from[character]:
            return True, directions[character]
        return False, "e"

    q = queue.Queue()
    q.put([s_r+1, s_c, "d", 1])
    q.put([s_r-1, s_c, "u", 1])
    q.put([s_r, s_c+1, "r", 1])
    q.put([s_r, s_c-1, "l", 1])

    while not q.empty():
        r, c, dir, step = q.get()
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            continue

        connects, next_dirs = connected(grid[r][c], dir)
        if connects and seen[r][c] == -1:
            seen[r][c] = step

            for next_dir in next_dirs:
                if next_dir == "l":
                    q.put([r, c-1, "l", step+1])
                elif next_dir == "r":
                    q.put([r, c+1, "r", step+1])
                elif next_dir == "u":
                    q.put([r-1, c, "u", step+1])
                elif next_dir == "d":
                    q.put([r+1, c, "d", step+1])

    # NOTE: This is hardcoded (the S)
    directions = {("|", "u"): "u", ("|", "d"): "d", ("-", "l"): "l", ("-", "r"): "r", ("J", "d"): "l", ("J", "r"): "u", ("L", "d"): "r", ("L", "l"): "u", ("7", "u"): "l", ("7", "r"): "d", ("F", "l"): "d", ("F", "u"): "r", ("S", "d"): "l"}

    def get_coords(r, c, dir):
        if dir == "u":
            r -= 1
        elif dir == "d":
            r += 1
        elif dir == "l":
            c -= 1
        elif dir == "r":
            c += 1
        return r, c
    
    def get_perp(r, c, dir):
        if dir == "u":
            c += 1
        elif dir == "d":
            c -= 1
        elif dir == "l":
            r -= 1
        elif dir == "r":
            r += 1
        return r, c
    
    def opposite_perp(r, c, dir):
        if dir == "u":
            c -= 1
        elif dir == "d":
            c += 1
        elif dir == "l":
            r += 1
        elif dir == "r":
            r -= 1
        return r, c

    def step_function(r, c, dir):
        r, c = get_coords(r, c, dir)
        return r, c, directions[grid[r][c], dir]
    
    def bfs(r, c):
        if seen[r][c] != -1:
            return 0
        total = 0
        q = queue.Queue()
        q.put([r, c])
        while not q.empty():
            r, c = q.get()
            if seen[r][c] == -1:
                seen[r][c] = -2
                total += 1
                q.put([r-1, c])
                q.put([r+1, c])
                q.put([r, c-1])
                q.put([r, c+1])
        return total

    def traverse(r, c, dir):
        prev_dir = dir
        r, c, dir = step_function(r, c, dir)
        res = 0
        while r != s_r or c != s_c:
            check_r, check_c = opposite_perp(r, c, prev_dir)
            crazy_r, crazy_c = opposite_perp(r, c, dir)
            res += bfs(check_r, check_c) + bfs(crazy_r, crazy_c)
            prev_dir = dir
            r, c, dir = step_function(r, c, dir)
        return res

    # NOTE: this is hardcoded (the "l" direction)
    total = traverse(s_r, s_c, "l")

    return total


if __name__ == '__main__':
    # print(part1())
    print(part2())
