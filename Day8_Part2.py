import sys

class Node:
    def __init__(self):
        self.children = []
        self.indexes = []
        self.metadata = 0

    def add_child(self, child):        
        self.children.append(child)        

    def get_children(self):
        return self.children
    
    def get_indexes(self):
        return self.indexes
    
    def get_metadata(self):
        return self.metadata
    
    def add_indexes(self, indexes):
        self.indexes += indexes
    
    def set_metadata(self, metadata):
        self.metadata = metadata

def build_tree(root, config, total_child, index_size):    
    if total_child == 0:        
        root.set_metadata(sum(config[:index_size]))        
        root.add_indexes([1])
        del config[:index_size]       
    else:
        while total_child > 0:
            child = Node()

            children = config[0]
            child_idx_size = config[1]

            del config[:2]

            (child, config) = build_tree(child, config, children, child_idx_size)
            root.add_child(child)

            total_child -= 1
        
        root.add_indexes(config[:index_size])

        sum_metadata = 0
        root_indexes = root.get_indexes()
        root_children = root.get_children()

        for i in root_indexes:
            if i > 0 and i <= len(root_children):   
                sum_metadata += root_children[i - 1].get_metadata()

        root.set_metadata(sum_metadata)

        del config[:index_size]

    return (root, config)

def read(filename):    
    with open(filename) as f:        
        return [int(x) for x in f.readline().split()]

if __name__ == '__main__':
    config = read(sys.argv[1])

    root = Node()
    total_child = config[0]
    index_size = config[1]
    del config[:2]

    (root, _) = build_tree(root, config, total_child, index_size)    
    print(root.get_metadata())