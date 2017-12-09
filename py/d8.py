output = None

with open('d8i.txt') as f:
    linesr = f.readlines()
#
#  linesr = """ b inc 5 if a > 1
#  a inc 1 if b < 5
#  c dec -10 if a >= 1
#  c inc -20 if c == 10 """.split("\n")

from collections import defaultdict

regi = defaultdict(int)

def process(reg, verb, jmp, reg2, comp, num):
    cond = eval(' '.join([str(regi[reg2]), comp, num]))
    #  print reg, verb, jmp, reg2, comp, num, str(cond)
    if not cond:
        return
    if verb == "inc":
        regi[reg] += int(jmp)
    else:
        regi[reg] -= int(jmp)
    return

vals = []
lines = []
for line in linesr:
    lines.append(line.strip())
    reg, verb, jmp, ifw, reg2, comp, num  = line.split()
    process(reg, verb, jmp, reg2, comp, num)
    import operator
    mv = max(regi.iteritems(), key=operator.itemgetter(1))
    vals.append(mv)


print max(vals, key=operator.itemgetter(1))
