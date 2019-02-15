#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $(basename $0) <file>"
  exit 1
fi
diff <(cat $1 | solutions/solution.py) <(cat $1 | solutions/build/runjava)
