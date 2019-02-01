#!/bin/sh
# modified from Charles' generate_testcase.sh
# https://github.com/z2oh/usc_lowerdivision_spring2018/blob/master/image_rotate/testcases/generate_testcase.sh

# make sure we are in the test case directory
cd "$(dirname "$0")"

if [ $# -eq 1 ] ; then
	CASES=$1
elif [ $# -gt 1 ]; then
	echo "USAGE: $0 <num>"
	exit 1
else
	CASES=20
fi

mkdir -p input output

if [ -e "input/input0.txt" ] || [ -e "output/output0.txt" ]; then
	echo "ERROR: '$INPUT_FILE' or '$OUTPUT_FILE' exists"
	printf "Overwrite? y/[n] "
	read force
	[ "$force" = y ] || exit 1
fi

for sample in $(seq 0 $CASES); do
	INPUT_FILE="./input/input$sample.txt"
	OUTPUT_FILE="./output/output$sample.txt"

	RAND_INPUT="$(./gen_input.py)"
	LINES="$(echo "$RAND_INPUT" | wc -l)"
	(echo "$LINES"; echo "$RAND_INPUT") > "$INPUT_FILE"
	solutions/solution.py < "$INPUT_FILE" > "$OUTPUT_FILE"
done

exec ./ensure_sanity.sh
