output = None

with open('d7i.txt') as f:
    linesr = f.readlines()

#  linesr = """pbga (66)
#  xhth (57)
#  ebii (61)
#  havc (66)
#  ktlj (57)
#  fwft (72) -> ktlj, cntj, xhth
#  qoyq (66)
#  padx (45) -> pbga, havc, qoyq
#  tknk (41) -> ugml, padx, fwft
#  jptl (61)
#  ugml (68) -> gyxo, ebii, jptl
#  gyxo (61)
#  cntj (57)""".split("\n")

s = {}
lines = []
for line in linesr:
    #  line = int(line)
    #  line = [int(x) for x in line.split()]
    lines.append(line.strip())

for line in lines:
    thing = line.split()
    name = thing[0]
    weight = int(thing[1][1:-1])
    if len(thing) > 2:
        children = ''.join(thing[3:]).split(",")
    else:
        children = []
    s[name] = {
        "weight": weight,
        "children": children
    }


print lines
print s

def put_weight(s, root):
    if len(s[root]["children"])==0:
        return s[root]["weight"]
    return s[root]["weight"] + sum((put_weight(s, c) for c in s[root]["children"]))

for k,v in s.iteritems():
    v["allchild"] = put_weight(s, k)
    for child in v["children"]:
        val = s[child].get("parent", None)
        if val is None:
            s[child]["parent"] = [k]
        else:
            s[child]["parent"].append(k)


master = None
for k,v in s.iteritems():
    if v.get("parent", None) is None:
        master = k
        break

def allsame(s, root):
    c = s[root]["children"]
    if len(c) == 0 or len(c) == 1:
        return True
    w2 = list(s[x]["allchild"] for x in c)
    if len(set(w2)) == 1:
        # they are all the same
        return True

    w = list(s[x]["weight"] for x in c)
    from collections import Counter
    counter = Counter(w2)
    #  print counter
    wwind = w2.index(min(counter, key=counter.get))
    #  print w, w[wwind]

    bestind = w2.index(max(counter, key=counter.get))
    name = s[root]["children"][wwind]
    allchildm = s[name]["allchild"] - s[name]["weight"]
    print w2[bestind] - allchildm
    return False

for k,v in s.iteritems():
    allsame(s, k)

#  we need to find a node which
#  the grandchildredn are the same
#  but the children are wrong
#  def ch_gc(s, root):
    #  if allsame(s, root):
        #  not what we want
        #  return False
    #  the children are not the same
        #  from collections import Counter
        #  counter = Counter(w)
        #  wrongw = w.index(min(counter, key=counter.get))
        #  rightw = w.index(max(counter, key=counter.get))
        #  wCHA = w[wrongw]
        #  wRI = w[rightw]
        #  print wRI
        #  return wRI
    #  else:
        #  return (sss(s, x) for x in c)
#
#
#  print s[master]["allchild"]
#  print s
#
#  print sss(s, master)













