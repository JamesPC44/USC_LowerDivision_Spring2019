#! /bin/sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"
pushd $SCRIPT_DIR
  mkdir ./input || rm -rf ./input/*
  mkdir ./output || rm -rf ./output/*
  for i in {2..20}; do
    ./gen_input.py > input/input$i.txt
    cat input/input$i.txt | ./solution/solution.py > output/output$i.txt
  done
  # Check if everything is correct
  pushd $SCRIPT_DIR/solution
    javac Solution.java
  popd
  for i in {2..20}; do
  # Just to make sure the two solutions come up with the same answer
    pushd $SCRIPT_DIR/solution
      cat ../input/input$i.txt | java Solution
    popd
      cat input/input$i.txt | ./solution/solution.py
  done
  cp $SCRIPT_DIR/sample-inputs/* $SCRIPT_DIR/input/
  cp $SCRIPT_DIR/sample-outputs/* $SCRIPT_DIR/output/
popd
