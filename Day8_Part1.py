import sys

def build_tree(config):
    stack = []
    
    stack.append((config[0], config[1]))
    del config[:2]

    sum_metadata = 0

    while len(stack):        
        (top_child, top_metadata) = stack[-1]
        if top_child == 0:
            sum_metadata += sum(config[:top_metadata])
            del config[:top_metadata]
            del stack[-1]
        else:
            stack[-1] = (top_child - 1, top_metadata)
            stack.append((config[0], config[1]))
            del config[:2]
    
    print (sum_metadata)

def read(filename):    
    with open(filename) as f:        
        return [int(x) for x in f.readline().split()]

if __name__ == '__main__':
    config = read(sys.argv[1])
    build_tree(config)