import math

def part1():
    f = open('inputs/day8.txt', 'r')
    sequence = f.readline().strip()
    g = {}
    f.readline()

    for x in f:
        pair = x.strip().split(" = ")
        key = pair[0]
        values = pair[1].replace("(", "").replace(")", "").split(", ")
        g[key] = values
    
    cur = "AAA"
    end = "ZZZ"
    i = 0
    steps = 0

    while cur != end:
        if sequence[i] == "L":
            cur = g[cur][0]
        else:
            cur = g[cur][1]
        steps += 1
        i += 1
        if i == len(sequence):
            i = 0
    
    return steps

def part2():
    f = open('inputs/day8.txt', 'r')
    sequence = f.readline().strip()
    g = {}
    f.readline()

    cur = []

    for x in f:
        pair = x.strip().split(" = ")
        key = pair[0]
        values = pair[1].replace("(", "").replace(")", "").split(", ")
        g[key] = values
        if key[2] == "A":
            cur.append(key)
    
    def find_path(cur):
        steps = 0
        i = 0
        path = []
        z_idx = 0
        while True:
            pairing = [i, cur]
            if pairing in path:
                return z_idx
            path.append(pairing)
            if sequence[i] == "L":
                cur = g[cur][0]
            else:
                cur = g[cur][1]
            
            steps += 1
            i += 1

            if cur[2] == "Z":
                z_idx = steps

            if i == len(sequence):
                i = 0

    z_indices = []
    for i in range(len(cur)):
        z_indices.append(find_path(cur[i]))
    
    return math.lcm(*z_indices)

if __name__ == '__main__':
    print(part1())
    print(part2())