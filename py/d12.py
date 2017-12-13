
with open('d12i.txt') as f:
    linesr = f.readlines()

lines = [x.strip() for x in linesr]

#  lines = """0 <-> 2
#  1 <-> 1
#  2 <-> 0, 3, 4
#  3 <-> 2, 4
#  4 <-> 2, 3, 6
#  5 <-> 6
#  6 <-> 4, 5""".split('\n')
print lines

from collections import defaultdict
d = defaultdict(list)

for line in lines:
    s = line.split()
    #  print s
    par = s[0]
    ch = [x.strip() for x in (' '.join(s[2:]).split(","))]
    #  print ch
    for c in ch:
        d[par].append(c)
        d[c].append(par)

for k,v in d.iteritems():
    d[k] = list(set(v))

i = 0
visited = []
tovisit = ["0"]
while True:
    print len(visited)
    #  print tovisit, visited
    if len(tovisit) == 0:
        i += 1
        if len(d.keys()) == len(visited):
            break
        else:
            more = ([a for a in d.keys() if a not in visited])
            tovisit.append(more[0])

    nex = tovisit.pop(0)
    if nex in visited:
        continue
    visited.append(nex)
    for v in d[nex]:
        tovisit.append(v)

import json
print json.dumps(d, indent=2)
print len(visited), visited
print i
