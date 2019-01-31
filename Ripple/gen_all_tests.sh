#! /bin/sh

for i in {3..20}; do
  # Leave off 0..2 because those are part of the documentation
  ./genripple.py > input/input$i.txt
done
./solve_all_tests.sh
