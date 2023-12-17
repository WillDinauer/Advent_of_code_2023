def dot(i, x, c, vals, springs, hash_dp, dot_dp):
    if tuple((i, x, c)) in dot_dp:
        return dot_dp[i, x, c]
    val = 0
    if c > 0:
        if c == vals[x]:
            val = recur(i+1, x+1, 0, vals, springs, hash_dp, dot_dp)
    else:
        val = recur(i+1, x, 0, vals, springs, hash_dp, dot_dp)
    dot_dp[i, x, c] = val
    return val

def hash(i, x, c, vals, springs, hash_dp, dot_dp):
    if tuple((i, x, c)) in hash_dp:
        return hash_dp[i, x, c]
    val = 0
    c += 1
    if x < len(vals):
        if c <= vals[x]:
            val = recur(i+1, x, c, vals, springs, hash_dp, dot_dp)
    hash_dp[i, x, c-1] = val
    return val

def recur(i, x, c, vals, springs, hash_dp, dot_dp):
    if i == len(springs):
        return 1 if x == len(vals) or (x == len(vals)-1 and vals[x] == c) else 0
    
    if springs[i] == ".":
        return dot(i, x, c, vals, springs, hash_dp, dot_dp)
    elif springs[i] == "#":
        return hash(i, x, c, vals, springs, hash_dp, dot_dp)
    else:
        d = dot(i, x, c, vals, springs, hash_dp, dot_dp)
        h = hash(i, x, c, vals, springs, hash_dp, dot_dp)
        return d + h

def part1():
    f = open('inputs/day12.txt', 'r')
    total = 0
    for x in f:
        springs = x.strip().split(" ")[0].strip(".")
        vals = x.strip().split(" ")[1].strip().split(",")
        for i in range(len(vals)):
            vals[i] = int(vals[i])
        total += recur(0, 0, 0, vals, springs, {}, {})
    return total

def part2():
    f = open('inputs/day12.txt', 'r')
    total = 0
    for x in f:
        s = x.strip().split(" ")[0]
        v = x.strip().split(" ")[1].strip().split(",")
        for i in range(len(v)):
            v[i] = int(v[i])

        springs, vals = [], []
        for i in range(5):
            for j in range(len(s)):
                springs.append(s[j])
            if i != 4:
                springs.append("?")
            for j in range(len(v)):
                vals.append(v[j])

        total += recur(0, 0, 0, vals, springs, {}, {})
    return total

if __name__ == '__main__':
    print(part1())
    print(part2())