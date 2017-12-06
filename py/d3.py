def move_right(x,y):
    return x+1, y

def move_down(x,y):
    return x,y-1

def move_left(x,y):
    return x-1,y

def move_up(x,y):
    return x,y+1

def move_upright(x,y):
    return move_up(*move_right(x,y))
def move_upleft(x,y):
    return move_up(*move_left(x,y))
def move_downright(x,y):
    return move_down(*move_right(x,y))
def move_downleft(x,y):
    return move_down(*move_left(x,y))

assert move_upright(0,0) == (1,1)

moves = [move_right, move_up, move_left, move_down]
diags = moves + [move_upright, move_upleft, move_downleft, move_downright]

def get_pos(end):
    from itertools import cycle
    _moves = cycle(moves)

    points = []
    n = 1
    pos = 0,0
    m = 1 # number of times to keep going in that direction
    points.append((n, pos))
    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(m):
                if n >= end:
                   return points
                n+=1
                pos = move(*pos)
                points.append((n, pos))
        m += 1
    return points
def manhattan_distance(start, end):
    sx, sy = start
    ex, ey = end
    return abs(ex - sx) + abs(ey - sy)

a = get_pos(312051)
print manhattan_distance((0,0), a[-1][1])

def neigh(points, pos):
    #  print point
    sum = 0
    for move in diags:
        v = move(*pos)
        #  print "move:", v, points[v]
        sum += points[v]
    return sum


from collections import defaultdict
def get_pos2(end):
    from itertools import cycle
    _moves = cycle(moves)

    points = defaultdict(int)

    n = 1
    pos = 0,0
    m = 1 # number of times to keep going in that direction
    points[pos] = n

    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(m):
                if n >= end:
                   return points, pos
                pos = move(*pos)
                print 'cursp', pos
                n = neigh(points, pos)
                points[pos] = n
                print "curn: ", n
        m += 1
    return points, (0,0)

b,x = get_pos2(23)
b,x = get_pos2(312051)
print b
print x

print manhattan_distance((0,0), x)
