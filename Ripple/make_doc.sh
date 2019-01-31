#! /bin/sh

latexmk -pdf -interaction=nonstopmode RippleProblem.tex
latexmk -c RippleProblem.tex
