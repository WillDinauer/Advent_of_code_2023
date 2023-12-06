import math

def part1():
    f = open("inputs/day6.txt", "r")
    time = f.readline().strip("Time: ").strip().split("     ")
    dist = f.readline().strip("Distance: ").strip().split("   ")

    for i in range(len(time)):
        time[i] = int(time[i])
        dist[i] = int(dist[i])

    totals = []

    for i in range(len(time)):
        total = 0
        for j in range(time[i]):
            speed = j
            time_to_travel = time[i]-j
            if speed * time_to_travel > dist[i]:
                total += 1
        totals.append(total)

    res = 1
    for t in totals:
        res *= t
    return res

def part2():
    f = open("inputs/day6.txt", "r")
    times = f.readline().strip("Time: ").strip().split("     ")
    dists = f.readline().strip("Distance: ").strip().split("   ")
    time = ""
    dist = ""
    for t in times:
        time += t
    for d in dists:
        dist += d
    time = int(time)
    dist = int(dist)

    # Quadratic formula
    b = -time
    a = 1
    c = dist
    x1 = (-b + math.sqrt(b**2-(4*a*c)))/(2*a)
    x2 = (-b -math.sqrt(b**2-(4*a*c)))/(2*a)

    return int(x1)-int(x2)

if __name__ == '__main__':
    print(part1())
    print(part2())