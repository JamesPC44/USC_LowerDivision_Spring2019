#!/bin/sh

make -C solutions/
for f in input/input*.txt; do
  echo "Test $(basename $f .txt)"
  of="$(echo $f | sed 's/input/output/g')"
  #of="output/$(basename $f .in).out"
  cat $f | solutions/solution.py > $of
  ./solution_diff.sh $f
done
