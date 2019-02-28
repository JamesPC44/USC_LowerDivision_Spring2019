#!/bin/sh
set -e
NUM_TESTS=$(ls input | sort -V | tail -1 | grep -o '[0-9]\+')

ensure_solution () {
	case $1 in
		*.java) printf "cd solution; java $(javac -verbose $1 2>&1| tail -2 | head -1 | sed 's#.*solution/\(.*\)\.class.*#\1#')";;
		*.c) gcc $solution -o solution/solution; printf "solution/solution";;
		*.hs) ghc $solution -o solution/haskell_solution -outputdir=/tmp > /dev/null; printf "solution/haskell_solution";;
		*) printf "%s" "$1";;
	esac
}

rm -f solution/*.class
for solution in solution/Solution.*; do
	solution="$(ensure_solution $solution)"
	echo "trying solution $solution"
	for i in $(seq 0 $NUM_TESTS); do
		[ "$(cat output/output$i.txt)" = "$(eval "$solution" < input/input$i.txt)" ] || {
			echo failed on test $i
			exit 1
		}
	done
done
echo success
