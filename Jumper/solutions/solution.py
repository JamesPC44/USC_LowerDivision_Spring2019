#! /usr/bin/env python3

# Hunter Damron 2019
# Solves the Jumper Problem

from sys import stderr
from numpy import float32
DEBUG = False
def debug(s):
    if DEBUG: print("DBG: %s" % s, file=stderr)

from math import sqrt

errorbound = 0.1

def main():
    v, n = (int(x) for x in input().split())
    xy = [(int(v) for v in input().split()) for i in range(n)]
    m = [float32(y / x) for x, y in xy]
    debug("v = %d, n = %d" % (v, n))
    debug("m = %s" % m)
    g = 10
    i = 0
    jumped = False
    count = 0
    while not jumped or i != 0 and count <= n:
        jumped = True
        # nextpos = i + m[i] * v**2 / g / sqrt(1 + m[i]**2)
        nextpos = float32(i - 2 * m[i] * v**2 / (g * (1 + float32(m[i]**2))))
        debug("%d to %f (%d)" % (i, nextpos, int(nextpos)))
        err = 0.5 - nextpos % 1
        if abs(err) > errorbound:
            print("ERROR: error too large %f" % err, file=stderr)
        i = int(nextpos)
        count += 1
    if count > n: print("ERROR: count too high", file=stderr)
    print(count)

if __name__ == "__main__":
    main()
