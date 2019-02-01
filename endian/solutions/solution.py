#!/usr/bin/env python3

from sys import stdin, stdout

def reverse(b):
    little = ((b & 0b11000000) >> 4) | ((b & 0b00110000) >> 4)
    little |= ((b & 0b00001100) << 4) | ((b & 0b00000011) << 4)
    return little.to_bytes(1, byteorder='little')

def main():
    data = stdin.buffer.read(1)
    while data:
        stdout.buffer.write(reverse(int.from_bytes(data, 'little')))
        data = stdin.buffer.read(1)

if __name__ == '__main__':
    main()
