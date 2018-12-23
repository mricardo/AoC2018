import sys

def incoming_edge(node, graph):
    for k in graph:
        if node in graph[k]:
            return True
    
    return False

def topological_sort(no_incoming, graph):
    sorted_elems = []

    while len(no_incoming) > 0:
        node = no_incoming[0]
        del no_incoming[0]

        sorted_elems.append(node)

        if node in graph:
            destinations = graph[node]
                        
            while len(destinations) > 0:
                d = destinations[0]
                destinations.remove(d)
                
                if not incoming_edge(d, graph):
                    no_incoming.append(d)
                    no_incoming.sort()
        
    return sorted_elems

def read(filename):    
    graph = {}
    with open(filename) as f:
        for line in f:           
            id1 = line[5:line.find(' ', 5)]
            idx = line.find('step') + 5
            id2 = line[idx:line.find(' ', idx)]
      
            if id1 not in graph:
                graph[id1] = []
            
            graph[id1].append(id2)
    
    no_incoming = []
    for node in graph:
        if (not incoming_edge(node, graph)):
            no_incoming.append(node)

    sorted_elems = topological_sort(no_incoming, graph)
    print(''.join(sorted_elems))

if __name__ == '__main__':
    read(sys.argv[1])