import sys
from datetime import datetime
import re
import collections

def date(elem):
    return datetime.strptime(elem[1:17], '%Y-%m-%d %H:%M')

def read(filename):
    records = []
    with open(filename) as f:
        for line in f:
            records.append(line)
    
    records.sort(key=date)
    return records

def summarise(records):
    r = re.compile('^\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})\] (.+)$')
    guards = {}
    max_guard = (-1,-1, [])
    i = 0
    while i < len(records):
        res = r.match(records[i])
        description = res.group(2)

        if description.find('#') != -1:
            guard = int(description[7:description.find(' ', 7)])
        else:
            minutes_start = int(res.group(1))
            
            i += 1
            res = r.match(records[i])
            minutes_end = int(res.group(1))
            elapsed = minutes_end - minutes_start
            
            if guard not in guards:
                guards[guard] = (0, [])
            
            guards[guard] = (guards[guard][0] + elapsed,  
                             guards[guard][1] + list(range(minutes_start, minutes_end)))

            if (guards[guard][0] > max_guard[1]):
                max_guard = (guard, guards[guard][0], guards[guard][1])

        i += 1
    
    guard_id = max_guard[0]
    minutes = max_guard[2]
    minutes.sort()
    
    counter = collections.Counter(minutes)

    common_minute = counter.most_common(1)[0][0]
    
    print(guard_id, common_minute)
    print(guard_id * common_minute)

if __name__ == '__main__':
    records = read(sys.argv[1])
    summarise(records)