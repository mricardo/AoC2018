import sys

def check_boxes(filename):
    boxes = []
    with open(filename) as fp:
        for f in fp:
            boxes.append(f)
    
    boxes.sort()
    i = 0
    while (i < len(boxes)):        
        j = 0
        while ((i != j) and (j < len(boxes))):
            z = 0
            differences = 0
            common = []
            while(z < len(boxes[i]) and z < len(boxes[j])):
                
                if ((ord(boxes[i][z]) - ord(boxes[j][z])) == 0):
                    common.append(boxes[i][z])
                else:
                    differences += 1
                    if (differences > 1):
                        break     
                z += 1     

            j += 1
            if (differences == 1):
                print("".join(common))
                return
        i += 1
            
if __name__ == '__main__':
    check_boxes(sys.argv[1])