import sys

def incoming_edge(node, graph):
    for k in graph:
        if node in graph[k]:
            return True
    
    return False

def decrease_counters(workers, counters):
    for w in workers:
        if w not in counters:
            counters[w] = 60 + (ord(w) - ord('A')) + 1
        counters[w] -= 1
    return counters

def filter_counters(counters):
    keys = []
    for c in counters:
        if counters[c] <= 0:
            keys.append(c)
    return keys

def topological_sort(workers, graph, max_workers, queue):    
    counters = {}    
    tick = 0
    while len(workers) > 0 or len(queue) > 0:
        while len(workers) < max_workers and len(queue) > 0:
            workers.append(queue[0])
            del queue[0]                
 
        counters = decrease_counters(workers, counters)        
        zero_counters = filter_counters(counters)
     
        tick += 1                     
            
        for k in zero_counters:            
            del workers[workers.index(k)]
            del counters[k]

            if k in graph:
                destinations = graph[k]
                
                while len(destinations) > 0:
                    d = destinations[0]
                    destinations.remove(d)

                    if not incoming_edge(d, graph):
                        if len(workers) < max_workers:
                            workers.append(d)
                        else:
                            queue.append(d)  
                          
    print("Time: ", tick)
    
def read(filename, max_workers):    
    graph = {}
    with open(filename) as f:
        for line in f:           
            id1 = line[5:line.find(' ', 5)]
            idx = line.find('step') + 5
            id2 = line[idx:line.find(' ', idx)]
      
            if id1 not in graph:
                graph[id1] = []
            
            graph[id1].append(id2)
    
    workers = []
    queue = []
    for node in graph:
        i = 0
        if (not incoming_edge(node, graph)):
            if i < max_workers:
                workers.append(node)
            else:
                queue.append(node)
    
    topological_sort(workers, graph, max_workers, queue)

if __name__ == '__main__':
    read(sys.argv[1], int(sys.argv[2]))