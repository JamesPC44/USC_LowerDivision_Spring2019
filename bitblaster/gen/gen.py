#!/usr/bin/python3

# Generates Testcases for the NimSolver, where the game value is not 0

import sys
import random as r

def nimsum(arr):
  ret = arr[0]
  for i in range(1, len(arr)):
    ret ^= arr[i]
  return ret

def main():
  if len(sys.argv) != 5:
    print("Usage: ./gen.py min_indicies max_indicies min_number max_number")
    #print(sys.argv)
    sys.exit(1)
  else:
    # Note that sys.argv[0] is the program name
    min_index = int(sys.argv[1])
    max_index = int(sys.argv[2])
    min_num = int(sys.argv[3])
    max_num = int(sys.argv[4])
    
    arr = []
    
    N = r.randint(min_index, max_index)
    
    for i in range(0,N):
      arr.append(r.randint(min_num, max_num))
      
    # Checks for the Nimsum not being 0. We want a nim game that is non-zero
    while nimsum(arr) == 0:
      idx = r.randint(0, N - 1)
      if arr[idx] > 1:
        arr[idx] -= 1 
      else:
        arr[idx] += 1
      
    print(str(N))
    for i in range(0, N):
      print(str(arr[i]))
  
main()
