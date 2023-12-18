class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.seen = set()
    def add(self, bundle):
        if (bundle[1], bundle[2], bundle[3], bundle[4]) in self.seen:
            return
        self.seen.add(tuple(bundle[1:5]))
        for i, b in enumerate(self.queue):
            if b[1] == bundle[1] and b[2] == bundle[2] and b[3] == bundle[3] and b[4] == bundle[4]:
                self.queue[i][0] = min(self.queue[i][0], bundle[0])
                return
        self.queue.append(bundle)
    def get(self):
        if self.empty():
            return None
        minimum = float('inf')
        min_idx = -1
        for i in range(len(self.queue)):
            if self.queue[i][0] < minimum:
                minimum = self.queue[i][0]
                min_idx = i
        return self.queue.pop(min_idx)
    def empty(self):
        return len(self.queue) == 0

def heuristic(r, c, grid):
    return len(grid)-1-r + len(grid[0])-1-c

def directions(r, c, dir, ct):
    res = []
    if dir == "r":
        res.append([r+1, c, "d", 1])
        res.append([r-1, c, "u", 1])
        if ct != 3:
            res.append([r, c+1, "r", ct+1])
    elif dir == "l":
        res.append([r+1, c, "d", 1])
        res.append([r-1, c, "u", 1])
        if ct != 3:
            res.append([r, c-1, "l", ct+1])
    elif dir == "u":
        res.append([r, c+1, "r", 1])
        res.append([r, c-1, "l", 1])
        if ct != 3:
            res.append([r-1, c, "u", ct+1])
    elif dir == "d":
        res.append([r, c+1, "r", 1])
        res.append([r, c-1, "l", 1])
        if ct != 3:
            res.append([r+1, c, "d", ct+1])
    return res

def part1():
    with open('inputs/day17.txt', 'r') as f:
        grid = [x.strip() for x in f]
        pq = PriorityQueue()
        pq.add([0, 0, 0, "r", 0, 0])
        while not pq.empty():
            val, r, c, dir, ct, cs = pq.get()
            if r == len(grid)-1 and c == len(grid[0])-1:
                return cs
            new_loc = directions(r, c, dir, ct)
            for bundle in new_loc:
                if bundle[0] < 0 or bundle[0] >= len(grid) or bundle[1] < 0 or bundle[1] >= len(grid[0]):
                    continue
                r = bundle[0]
                c = bundle[1]
                bundle.insert(0, cs + int(grid[r][c]) + heuristic(r, c, grid))
                bundle.append(cs+int(grid[r][c]))
                pq.add(bundle)
        return 0

def new_directions(r, c, dir, ct):
    res = []
    if dir == "r":
        if ct < 10:
            res.append([r, c+1, "r", ct+1])
        if ct > 3:
            res.append([r+1, c, "d", 1])
            res.append([r-1, c, "u", 1])
    elif dir == "l":
        if ct < 10:
            res.append([r, c-1, "l", ct+1])
        if ct > 3:
            res.append([r+1, c, "d", 1])
            res.append([r-1, c, "u", 1])
    elif dir == "u":
        if ct < 10:
            res.append([r-1, c, "u", ct+1])
        if ct > 3:
            res.append([r, c+1, "r", 1])
            res.append([r, c-1, "l", 1])
    elif dir == "d":
        if ct < 10:
            res.append([r+1, c, "d", ct+1])
        if ct > 3:
            res.append([r, c+1, "r", 1])
            res.append([r, c-1, "l", 1])
    return res

def part2():
    with open('inputs/day17_s.txt', 'r') as f:
        grid = [x.strip() for x in f]
        pq = PriorityQueue()
        pq.add([0, 0, 0, "r", 0, 0])
        pq.add([0, 0, 0, "d", 0, 0])
        while not pq.empty():
            val, r, c, dir, ct, cs = pq.get()
            # print(f"cs: {cs} r: {r} c: {c}")
            if r == len(grid)-1 and c == len(grid[0])-1:
                return cs
            new_loc = new_directions(r, c, dir, ct)
            for bundle in new_loc:
                if bundle[0] < 0 or bundle[0] >= len(grid) or bundle[1] < 0 or bundle[1] >= len(grid[0]):
                    continue
                r = bundle[0]
                c = bundle[1]
                bundle.insert(0, cs + int(grid[r][c]) + heuristic(r, c, grid))
                bundle.append(cs+int(grid[r][c]))
                pq.add(bundle)
        return 0
if __name__ == '__main__':
    print(part1())
    print(part2())