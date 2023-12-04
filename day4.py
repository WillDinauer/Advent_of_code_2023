def part1():
    f = open("inputs/day4.txt", "r")
    total = 0

    for x in f:
        line = x.strip()
        line = line.split("|")
        first = line[0].strip().split(": ")[1].split(" ")
        second = line[1].strip().split()

        cur = 0
        for num in second:
            if num in first:
                if cur == 0:
                    cur = 1
                else:
                    cur *= 2
        total += cur

    return total


def part2():
    f = open("inputs/day4.txt", "r")

    lines = 211
    total = 0
    cards = [1 for i in range(lines)]
    ct = 0

    for x in f:
        line = x.strip()
        line = line.split("|")
        first = line[0].strip().split(": ")[1].split(" ")
        second = line[1].strip().split()

        cur = 0
        for num in second:
            if num in first:
                cur += 1
        for i in range(cur):
            if ct+i == lines-1:
                break
            cards[ct+i+1] += cards[ct]
        total += cards[ct]
        ct += 1

    return total

if __name__ == '__main__':
    print(part1())
    print(part2())