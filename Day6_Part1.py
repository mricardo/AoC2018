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

def manhattan_distance_min(curr_coord, fixed_coords):
    mark_cell = ()
    total_min = None
    
    for (idd, fixed_x, fixed_y) in fixed_coords:
        if ((fixed_x, fixed_y) != curr_coord):
            d = manhattan_distance(curr_coord, (fixed_x, fixed_y))
            if not total_min or total_min > d:
                mark_cell = idd
                total_min = d                
            elif total_min == d:                 
                mark_cell = 0
        else:            
            mark_cell = idd
            break
   
    return mark_cell

def run_algo(coords, max_x, max_y):
    plane = [[0 for x in range(max_x)] for y in range(max_y )]

    count_coords = {}
    for c in coords:
        plane[c[2]][c[1]] = c[0]
        count_coords[c[0]] = 1
    
    left = right = top = bottom = []
    
    y = 0
    while y < max_y:
        x = 0
        while x < max_x:
            if plane[y][x] == 0:
                idd = manhattan_distance_min((x, y), coords)
                plane[y][x] = int(idd)  
                if idd != 0:              
                    count_coords[int(idd)] += 1                                
            x += 1
        y += 1
    
    left = set([i[0] for i in plane])
    right = set([i[-1] for i in plane])
    top = set(plane[0])
    bottom = set(plane[-1])

    max_c = None
    for c in count_coords:
        if c not in left and c not in right and c not in top and c not in bottom:
            if not max_c or count_coords[c] > max_c:
                max_c = count_coords[c]            

    print(max_c)  

if __name__ == '__main__':
    res = read(sys.argv[1])
    run_algo(res[0], res[1], res[2])