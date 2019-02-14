#! /usr/bin/env python3
# Justin Baum 2019

from random import randint

n = randint(3, 100)

board = [[randint(0,1) for i in range(n)] for j in range(n)]

print(n)

for row in board:
  for column in row:
    print(column, end="")
  print()
