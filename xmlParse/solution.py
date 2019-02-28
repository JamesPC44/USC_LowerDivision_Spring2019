from sys import stdin
from re import findall

stack = []
for line in stdin.readlines():
    for tag in findall('<[^>]+>', line):
        if tag[0] != '<':
            quit("error: bad regular expression")
        closing = tag[1] == '/'
        assert tag.index('>') + 1 == len(tag)
        name = tag[1 + closing:-1]
        if closing:
            if stack[-1] != name:
                quit("error: invalid xml (found closing tag for %s, expected %s)"
                        % (name, stack[-1]))
            print(stack.pop(), len(stack))
        else:
            stack.append(name)
