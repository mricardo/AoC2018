import sys
import re

MAX = 5000

def fill(fabric, idd, left, top, width, height):
    row, col = top, left
    
    while (row < top + height):
        while (col < left + width):
            fabric[row][col] = idd if fabric[row][col] == '.' else 'X'           
            col += 1
        row += 1
        col = left

def overlapping(fabric):
    count = row = 0
    
    while (row < MAX):
        count += fabric[row].count('X')
        row += 1
    return count

def sqr_inches(fabric, filename):    
    r = re.compile("^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$")

    with open(filename) as f:
        for line in f:        
            m = r.match(line)
            fill(fabric, int(m.group(1)), int(m.group(2)),  int(m.group(3)), int(m.group(4)), int(m.group(5)))

    return overlapping(fabric)

if __name__ == '__main__':
    fabric = [['.' for col in range(MAX)] for row in range(MAX)]
    print(sqr_inches(fabric, sys.argv[1]))