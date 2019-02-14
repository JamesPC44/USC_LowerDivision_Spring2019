#! /usr/bin/env python3

from sys import stdin, stdout

# Get board
def getboard(board, n):
  for i in range(n):
    line = stdin.readline()
    board[i] = list(map(lambda x: int(x), list(line)[:n]))

# Solution
def main():
  n = int(stdin.readline())
  # Get an array like structure
  board = [[0 for i in range(n)] for j in range(n)]
  getboard(board, n)
  # Solution
  numtips = 0
  for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
      if board[i][j] != (i+j) % 2: # Not the correct square so flip all above and to the left
        numtips += 1
        for ii in range(i+1):
          for jj in range(j+1):
            board[ii][jj] += 1
            board[ii][jj] %= 2
  print(numtips)


if __name__ == '__main__':
    main()
