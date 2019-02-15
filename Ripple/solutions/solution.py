#! /usr/bin/env python3

# Hunter Damron 2019
# Solves the Ripple Problem

from itertools import chain

def pworld(world, cancel=True):
    return "\n".join(reversed(["".join(str(int(x%2) if cancel else x%10) for x in row) for row in world]))

def pblocks(world):
    return "\n".join(reversed(["".join('■' if x%2 == 1 else '□' for x in row) for row in world]))

def main():
    w, h, n = (int(x) for x in input().split())
    txy = [(int(x) for x in input().split()) for i in range(n)]
    tf = int(input())
    world = [[0] * w for i in range(h)]
    for t, x, y in txy:
        dt = tf - t + 1
        if dt == 1:
            world[y][x] += 1
        else:
            diagonals = (((x-i, y+dt-i-1), (x+dt-i-1, y+i), (x+i, y-dt+i+1), (x-dt+i+1, y-i)) for i in range(dt-1))
            for x, y in chain(*(diagonals)):
                world[y % h][x % w] += 1

    wavesum = sum(x for x in chain(*world) if x % 2 == 1)

    # print("%s\n\n%s\n" % (pworld(world, cancel=False), pworld(world)))
    print("%s" % pblocks(world))
    print(wavesum)

if __name__ == "__main__":
    main()
