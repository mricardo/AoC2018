import sys
import re

MAX = 5000
non_overlap = -1
def fill(fabric, idd, left, top, width, height):
    row, col = top, left
    
    while (row < top + height):
        while (col < left + width):
            if (fabric[row][col] != '.'):
                fabric[row][col] += ',' + idd
            else:
                fabric[row][col] = idd
            col += 1
        row += 1
        col = left

def non_overlapping(fabric, idds):
    row = col = 0
    colliding_ids = []
    while (row < MAX):       
        while (col < MAX):                        
            if (',' in fabric[row][col]):                              
                colliding_ids += fabric[row][col].split(',')
            col += 1
        row += 1
        col = 0
        
    for i in idds:
        if i not in colliding_ids:
            return i
    return -1

def sqr_inches(fabric, filename):    
    r = re.compile("^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$")
    idds = []
    with open(filename) as f:
        for line in f:        
            m = r.match(line)
            idd = m.group(1)
            fill(fabric, idd, int(m.group(2)),  int(m.group(3)), int(m.group(4)), int(m.group(5)))
            idds.append(idd)

    return non_overlapping(fabric, idds)

if __name__ == '__main__':
    fabric = [['.' for col in range(MAX)] for row in range(MAX)]
    print(sqr_inches(fabric, sys.argv[1]))