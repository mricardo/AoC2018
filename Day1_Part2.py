import sys

def read_changes(filename):
    changes = []
    with open(filename) as fp:
        for f in fp:                   
            changes.append(int(f))
    
    return changes 

def apply_changes(changes):
    found = False
    frequency = 0
    counter = {}
    counter[0] = 1
    while(found == False):
        for c in changes:
            frequency += c
   
            if (frequency in counter):
                counter[frequency] += 1
            else:
                counter[frequency] = 1
            
            if (counter[frequency] == 2):
                print(frequency)
                found = True
                break
            
if __name__ == "__main__":
    changes = read_changes(sys.argv[1])
    apply_changes(changes)