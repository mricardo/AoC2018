import sys

def part1(filename):
    frequency = 0
    with open(filename) as fp:
        for f in fp:                   
            frequency += int(f)
    
    print(frequency)
            
if __name__ == "__main__":
    part2(sys.argv[1])