import sys

def merge(line):
    i = 0
    l1 = len(line)
    p = ''
    while i < l1:
        c = line[i]
        
        if not p:
            p += c
        else:
            if ((p[-1] == c) or (p[-1].lower() != c.lower())):
                p += c
            else:
                p = p[:-1]
        i += 1
    l2 = len(p)
    
    return (p, l1 != l2)

def polymer(filename):
    line = ''
    with open(filename) as f:
        line = f.readline()
    
    rep_lc = list(range(ord('a'), ord('z')))
    rep_up = list(range(ord('A'), ord('Z')))
    min_l = len(line)
    i = 0
    while i < len(rep_lc):        
        pattern = line[:].replace(chr(rep_lc[i]), '')
        pattern = pattern.replace(chr(rep_up[i]), '')
        l = True
        while l:
            (pattern, l) = merge(pattern)
            if len(pattern) < min_l:
                min_l = len(pattern)
        i += 1
    print(min_l)

if __name__ == '__main__':
    polymer(sys.argv[1])