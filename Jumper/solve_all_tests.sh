#!/bin/sh

make -C solutions
for f in input/input*.txt; do
  of="$(echo $f | sed 's/input/output/g')"
  cat $f | solutions/solution.py > $of
  cat $f | solutions/build/solution | diff $of -
  cat $f | java -cp solutions/build solution | diff $of -
done
