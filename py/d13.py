
import json
from collections import defaultdict
with open('d13i.txt') as f:
    linesr = f.readlines()

lines = [x.strip() for x in linesr]

#  lines = """0: 3
#  1: 2
#  4: 4
#  6: 4""".split('\n')
print lines

d = defaultdict(list)

for line in lines:
    s = [x.strip() for x in line.split(":")]
    d[int(s[0])] = ['S'] + [' ' for _ in range(int(x[1])-1)]
print d

def move(la):
    for k,v in la.iteritems():
        if len(v) == 1:
            continue
        if len(v) == 2:
            n = v[0]
            v[0] = v[1]
            v[1] = v[0]
            continue
        if 'S' in v:
            # move forward
            old = (v.index('S'))
            nx = (old + 1)
            v[nx] = "s" if nx == len(v)-1 else "S"
        else: # backward
            old = (v.index('s'))
            nx = (old - 1)
            v[nx] = "S" if nx == 0 else "s"
        v[old] = " "
        la[k] = v
    return la

score = 0
highest = max(d.keys())
caught = [0 for _ in range(len(d.keys()))]
#  print highest
#  print d
for i in range(int(highest+1)):
    #  print d
    d = move(d)
    #  print d
    if (i) not in d.keys():
        continue
    for j, k in enumerate(d.keys()):
        if int(k) != i:
            continue
        if len(d[k]) == 1:
            caught[j] = 1
            continue
        if d[k][1] == "S":
            caught[j] = 1

print caught
for i, c in enumerate(caught):
    k = d.keys()[i]
    v = d[k]
    score += c * int(d.keys()[i])*int(len(d[k]))

#  print json.dumps(d, indent=2)
print score


def func(lines, dlay):
    total = 0
    for line in lines:
        layer, depth = list(map(int, line.split(": ")))
        if (layer+dlay) % ((depth - 1)*2) == 0:
            total += layer*depth
            if dlay != 0:
                return -1
    return total

curd = 0
while True:
    o = func(lines, curd)
    if curd == 0:
        print o
    if o == 0:
        break
    curd += 1
print curd
