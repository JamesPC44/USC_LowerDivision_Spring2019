#!/bin/sh

for f in input/input*.txt; do
  of="$(echo $f | sed 's/input/output/g')"
  #of="output/$(basename $f .in).out"
  cat $f | solutions/solution.py > $of
done
