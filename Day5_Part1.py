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
   
    l = True
    while l:
        (line, l) = merge(line)
        
    print(len(line))

if __name__ == '__main__':
    polymer(sys.argv[1])