#!/usr/bin/env python

from random import randrange

OUTPUT_SIZE = 2**16

def main(size):
    return ''.join(chr(randrange(0, 256)) for _ in range(size))

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("size", nargs='?', type=int, default=OUTPUT_SIZE)
    print(main(parser.parse_args().size), end='')
