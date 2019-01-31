#! /usr/bin/env python3

# Hunter Damron 2019
# Generates input files for Ripple Problem

from random import randint
from ripplevars import *

def main():
    w = randint(1, maxw)
    h = randint(1, maxh)
    n = randint(1, maxn)
    t, x, y = zip(*((randint(0, maxt-1), randint(0,w-1), randint(0, h-1)) for i in range(n)))
    t_f = randint(max(t)+1, maxt)

    s = ("%d %d %d\n" % (w, h, n)) + "\n".join("%d %d %d" % txy_i for txy_i in zip(t, x, y)) + ("\n%d" % t_f)
    print(s)

if __name__ == "__main__":
    main()
