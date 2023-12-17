def hash(s):
    total = 0
    for c in s:
        total = ((total + ord(c)) * 17) % 256
    return total

def part1():
    with open('inputs/day15.txt', 'r') as f:
        strings = f.readline().strip().split(",")
        total = 0
        for s in strings:
            total += hash(s)
        return total

def part2():
    with open('inputs/day15.txt', 'r') as f:
        strings = f.readline().strip().split(",")
        total = 0
        hmap = {}
        for i in range(256):
            hmap[i] = []

        for s in strings:
            if "=" in s:
                label = s.strip().split("=")[0]
                box = hash(label)
                labels = [lens[0] for lens in hmap[box]]
                if label in labels:
                    hmap[box][labels.index(label)][1] = int(s[-1])
                else:
                    hmap[box].append([label, int(s[-1])])
            else:
                label = s[:len(s)-1]
                box = hash(label)
                labels = [lens[0] for lens in hmap[box]]
                if label in labels:
                    hmap[box].pop(labels.index(label))

        for box_num in range(256):
            l = hmap[box_num]
            for i, item in enumerate(l):
                total += (box_num+1) * (i+1) * (item[1])
        return total

if __name__ == '__main__':
    print(part1())
    print(part2())