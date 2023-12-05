
def part1():

    f = open("inputs/day5.txt", "r")

    seeds = f.readline().strip("seeds: ").strip().split(" ")
    for i in range(len(seeds)):
        seeds[i] = int(seeds[i])

    def transition(name):
        line = f.readline().strip()
        while line != name:
            line = f.readline().strip()
        line = f.readline().strip()
        grid = []
        while line != "":
            nums = line.split(" ")
            for i in range(3):
                nums[i] = int(nums[i])
            grid.append(nums)
            line = f.readline().strip()
        for i in range(len(seeds)):
            seed = seeds[i]
            for r in range(len(grid)):
                if seed >= grid[r][1] and seed <= grid[r][1] + grid[r][2]:
                    seeds[i] = grid[r][0] + (seed - grid[r][1])
                    break
    map_names = ["seed-to-soil map:","soil-to-fertilizer map:","fertilizer-to-water map:","water-to-light map:","light-to-temperature map:","temperature-to-humidity map:","humidity-to-location map:"]

    for map in map_names:
        transition(map)
    return min(seeds)

def part2():
    f = open("inputs/day5.txt", "r")

    first = f.readline().strip("seeds: ").strip().split(" ")
    seeds = []
    for i in range(0, len(first), 2):
        seeds.append([int(first[i]), int(first[i]) + int(first[i+1]) - 1])

    def intersecting(pair, row):
        left = max(pair[0], row[1])
        right = min(pair[1], row[1]+row[2]-1)

        if right < left:
            return []
        return [left, right]
    
    def update_unmapped(unmapped, seedlet):
        new_unmapped = []
        for pair in unmapped:
            stay = True
            if seedlet[0] >= pair[0] and seedlet[0] <= pair[1]:
                stay = False
                if pair[0] != seedlet[0]:
                    new_unmapped.append([pair[0], seedlet[0]-1])
            if seedlet[1] <= pair[1] and seedlet[1] >= pair[0]:
                stay = False
                if pair[1] != seedlet[1]:
                    new_unmapped.append([seedlet[1]+1, pair[1]])
            if stay:
                new_unmapped.append(pair)
        return new_unmapped       
    
    def transition(name):
        nonlocal seeds
        line = f.readline().strip()
        while line != name:
            line = f.readline().strip()
        line = f.readline().strip()
        grid = []
        while line != "":
            nums = line.split(" ")
            for i in range(3):
                nums[i] = int(nums[i])
            grid.append(nums)
            line = f.readline().strip()
        
        new_seeds = []
        for pair in seeds:
            unmapped = [pair.copy()]
            for r in range(len(grid)):
                seedlet = intersecting(pair, grid[r])
                if len(seedlet) > 0:
                    unmapped = update_unmapped(unmapped, seedlet)
                    new_seeds.append([grid[r][0] + (seedlet[0]-grid[r][1]), grid[r][0] + (seedlet[1]-grid[r][1])])
            for pair in unmapped:
                new_seeds.append(pair)
        seeds = new_seeds
    
    map_names = ["seed-to-soil map:","soil-to-fertilizer map:","fertilizer-to-water map:","water-to-light map:","light-to-temperature map:","temperature-to-humidity map:","humidity-to-location map:"]

    for map in map_names:
        transition(map)
    
    return min(seeds[0:])[0]

if __name__ == '__main__':
    print(part1())
    print(part2())