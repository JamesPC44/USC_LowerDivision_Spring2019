#! /bin/sh

latexmk -pdf -interaction=nonstopmode JumperProblem.tex
latexmk -c JumperProblem.tex
