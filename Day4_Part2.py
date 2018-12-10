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
    
    minutes = []
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
        
            range_minutes = list(range(minutes_start, minutes_end))

            for m in range_minutes:
                minutes.append((guard, m))

        i += 1
    
    counter = collections.Counter(minutes)

    common_minute = counter.most_common(1)[0][0]
    guard = common_minute[0]
    minute = common_minute[1]
    print(guard * minute)

if __name__ == '__main__':
    records = read(sys.argv[1])
    summarise(records)