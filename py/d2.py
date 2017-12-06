
import operator

with open('d2i.txt') as f:
    lines = f.readlines()
numlist = [[int(x) for x in line.split()] for line in lines]

def checksum(ns):
    mn, mx = (min(ns), max(ns) )
    return mx - mn

def evdiv(ns):
    for i, m in enumerate(ns):
        for j, n in enumerate(ns):
            if i == j:
                continue
            if m % n == 0:
                return m / n
    print "ERROR"
    return 0

def cslist(nss):
    #  sums = map(checksum, nss)
    sums = map(evdiv, nss)
    return reduce(operator.add, sums, 0)


#  numlist = [
    #  [5,1,9,5],
    #  [7,5,3],
    #  [2,4,6,8]
#  ]
print cslist(numlist)
