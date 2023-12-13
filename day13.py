def mirror_row(grid, a, b):
    if a < 0 or b >= len(grid):
        return True
    for c in range(len(grid[a])):
        if grid[a][c] != grid[b][c]:
            return False
    return mirror_row(grid, a-1, b+1)

def mirror_col(grid, a, b):
    if a < 0 or b >= len(grid[0]):
        return True
    
    for r in range(len(grid)):
        if grid[r][a] != grid[r][b]:
            return False
    return mirror_col(grid, a-1, b+1)

def compute_note(grid):
    for r in range(1, len(grid)):
        if mirror_row(grid, r-1, r):
            return r*100
            
    for c in range(1, len(grid[0])):
        if mirror_col(grid, c-1, c):
            return c
    
def part1():
    with open('inputs/day13.txt', 'r') as f:
        line = f.readline()

        total = 0
        while line:
            grid = []
            while line.strip() != "":
                grid.append(line.strip())
                line = f.readline()
            total += compute_note(grid)
            line = f.readline()
        return total
    
def compute_p2(grid, original_val):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            grid[row][col] = "#" if grid[row][col] == "." else "."
            for r in range(1, len(grid)):
                if mirror_row(grid, r-1, r) and r*100 != original_val:
                    return r*100
            
            for c in range(1, len(grid[0])):
                if mirror_col(grid, c-1, c) and c != original_val:
                    return c
            grid[row][col] = "#" if grid[row][col] == "." else "."
    
def part2():
    with open('inputs/day13.txt', 'r') as f:
        line = f.readline()

        total = 0
        while line:
            grid = []
            while line.strip() != "":
                x = line.strip()
                row = []
                for i in range(len(x)):
                    row.append(x[i])
                grid.append(row)
                line = f.readline()
            original_val = compute_note(grid)
            total += compute_p2(grid, original_val)
            line = f.readline()
        return total
    
if __name__ == '__main__':
    print(part1())
    print(part2())