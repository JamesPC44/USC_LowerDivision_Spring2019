#! /bin/sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"
pushd $SCRIPT_DIR
  mkdir ./input || rm -rf ./input/*
  mkdir ./output || rm -rf ./output/*
  for i in {1..20}; do
    python3 ./gen_input.py > input/input$i.txt
    cat input/input$i.txt | python3 ./solution/solution.py > output/output$i.txt
  done
popd

