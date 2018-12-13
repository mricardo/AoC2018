import sys

def read(filename):
    coords = []
    max_x = None
    max_y = None
    with open(filename) as f:
        for line in f:
            comma = line.find(',')
            x, y = int(line[:comma]), int(line[comma+1:])
            max_x = x if (not max_x or x > max_x) else max_x
            max_y = y if (not max_y or y > max_y) else max_y
            coords.append(((len(coords) + 1), x, y))
    
    return (coords, max_x + 1, max_y + 1)

def manhattan_distance(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

def manhattan_distance_within(curr_coord, fixed_coords, distance):
    sum_d = 0
    
    for (_, fixed_x, fixed_y) in fixed_coords:
        d = manhattan_distance(curr_coord, (fixed_x, fixed_y))
        sum_d += d  
    
    if (sum_d < distance):        
        return True
    
    return False

def run_algo(coords, max_x, max_y, distance):        
    region = 0
    
    y = 0
    while y < max_y:
        x = 0
        while x < max_x:
            if True:
                within = manhattan_distance_within((x, y), coords, distance)
                if within:                    
                    region += 1                           
            x += 1
        y += 1

    print(region)

if __name__ == '__main__':
    res = read(sys.argv[1])
    run_algo(res[0], res[1], res[2], int(sys.argv[2]))