#! /usr/bin/env python3

from sys import stderr, argv
DEBUG = False
def debug(s):
    if DEBUG: print("DBG: %s" % s, file=stderr)

from random import randint, choice, seed
from math import sqrt, ceil
from jumpervars import *

def fitslope(m, maxxy):  # TODO get integer approximation
    besterr = maxxy**2
    bestpair = (1, 0)
    for x in range(1, int(min(maxxy, maxxy/abs(m)))):
        y = round(x*m)
        err = abs(y/x - m)
        if err < besterr:
            besterr = err
            bestpair = (x,y)
    if (bestpair == (1, 0)):
        print("ERROR: could not properly estimate slope %f with rationals" % m, file=stderr)
    return bestpair


def main():
    if len(argv) > 1:
        seed(int(argv[1]))
    n = randint(1, maxn)  # TODO start from 1
    soln = randint(1, n)

    used = [False] * n
    used[0] = True
    jumps = [0]

    for i in range(soln-1):
        nextpos = choice([i for i, u in enumerate(used) if not u])
        used[nextpos] = True
        jumps.append(nextpos)
    jumps.append(0)
    maxd = max(abs(p2 - p1 + 0.5) for p1, p2 in zip(jumps,jumps[1:]))
    minv = sqrt(maxd * g)
    debug("minv = %f" % minv)
    v = randint(ceil(minv), maxv)
    debug("Order: %s" % jumps)

    slopes = [None] * n
    for p1, p2 in zip(jumps,jumps[1:]):
        d = p2 - p1
        neg = p2 - p1 < 0  # Resultant x should be negative
        d += 0.5  # To land right in the middle of the range

        # m = d * g / sqrt(v**4 - d**2 * g**2)
        m = (-v**2 + choice((-1,1)) * sqrt(v**4 - (d*g)**2)) / (d*g)
        x, y = fitslope(m, maxxy)
        debug("Slope %d = %f (%d/%d = %f)" % (p1, m, y, x, y/x))
        slopes[p1] = (x, y)
    for i in (i for i, u in enumerate(used) if not u):
        x = choice((-1,1)) * randint(1, maxxy)
        y = randint(0, maxxy)
        slopes[i] = x, y
        debug("Unused slope %d = %d/%d = %f" % (i, y, x, y/x))

    print("%d %d" % (v, n))
    print("\n".join("%d %d" % m for m in slopes))
    print("ANSWER = %d" % soln, file=stderr)

if __name__ == "__main__":
    main()
