import sys

def checksum(filename):
    total_count_2 = 0
    total_count_3 = 0
    with open(filename) as fp:
        for f in fp:
            count_2 = 0
            count_3 = 0
            
            while (len(f) > 0):                
                count = f.count(f[0])
                if (count == 2 and count_2 == 0):
                    count_2 += 1
                elif (count == 3 and count_3 == 0):
                    count_3 += 1
                f = f.replace(f[0], "")

            total_count_2 += count_2
            total_count_3 += count_3

    print (total_count_2 * total_count_3)
            
if __name__ == '__main__':
    checksum(sys.argv[1])