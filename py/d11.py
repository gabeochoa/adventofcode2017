
inp = open('d11i.txt','r').read().rstrip().split(",")
#  inp = ['ne', 'ne', 'ne']

class Hex(object):
    def __init__(self, q, r):
        self.q = q
        self.r = r
    def get_neighbor(self, direction):
        return Hex(self.q + direction.q, self.r + direction.r)
h_dir = [
   Hex(+1,  0), Hex(+1, -1), Hex( 0, -1),
   Hex(-1,  0), Hex(-1, +1), Hex( 0, +1)
]
dirs = {
    "n" : h_dir[2],
    "ne" : h_dir[1],
    "se" : h_dir[0],
    "s" : h_dir[5],
    "sw" : h_dir[4],
    "nw" : h_dir[3],
}

def hex_distance(a, b):
    return (abs(a.q - b.q)
          + abs(a.q + a.r - b.q - b.r)
          + abs(a.r - b.r)) / 2

def disthex(inputs):
    orig= Hex(0, 0)
    cur = orig
    ma = 0
    for move in inputs:
        cur = cur.get_neighbor(dirs[move])
        a = hex_distance(cur, orig)
        if a > ma:
            ma = a
    print cur.q, cur.r
    print "last dist: ", hex_distance(cur, orig)
    print "furthest: ", ma

disthex(inp)
