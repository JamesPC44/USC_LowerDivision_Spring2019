Ripple Problem
==============

Hunter Damron 2019

* RippleProblem.(tex|pdf) --  problem statement along with sample inputs and corresponding outputs
* genripple.py -- used to generate problem inputs (to stdout)
* solve_all_tests.sh -- short script to supply solutions to all samples (for use in the problem statement which displays samples 1-3)
* gen_all_tests.sh -- uses genripple.py to generate tests 3-20 (not 0-2 as those are in the docs) then solve_all_tests.sh to provide solutions
* solutions/solution.py -- my solution in python to the problem (complexity ~ n*t_f for n objects and finish time t_f)
* input/ -- directory with sample inputs as input*.txt
* output/ -- directory with corresponding sample outputs as output*.txt
* ripplevars.py -- declaration of maximum values for problem inputs (used by the problem statement and genripple.py; spaces are important!)
