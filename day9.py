def part1():
    f = open('inputs/day9.txt', 'r')

    def next_value(nums):
        diffs = []
        recur = False
        for i in range(1, len(nums)):
            diffs.append(nums[i]-nums[i-1])
            if nums[i] - nums[i-1] != 0:
                recur = True
        if recur:
            return nums[-1] + next_value(diffs)
        return nums[-1]

    total = 0
    for x in f:
        nums = x.strip().split(" ")
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        total += next_value(nums)
    return total

def part2():
    f = open('inputs/day9.txt', 'r')

    def next_value(nums):
        diffs = []
        recur = False
        for i in range(1, len(nums)):
            diffs.append(nums[i]-nums[i-1])
            if nums[i] - nums[i-1] != 0:
                recur = True
        if recur:
            return nums[-1] + next_value(diffs)
        return nums[-1]

    total = 0
    for x in f:
        nums = x.strip().split(" ")
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        nums.reverse()
        total += next_value(nums)
    return total

if __name__ == '__main__':
    print(part1())
    print(part2())