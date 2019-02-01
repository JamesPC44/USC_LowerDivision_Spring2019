# Byte Switcher
You have the answers to the final exam, but it's all junk!
You ask the professor and he tells you it was written on the PDP-11 back in the 80s.
Every byte value (or 'machine word') is stored strangely:
it uses 'middle-endian' order; that is,
if the order on a little-endian Intel CPU would be DCBA,
the order on a PDP-11 would be BADC.

For every input, convert the binary from middle- to little-endian.

## Input Format
The input will contain between $1$ and $2^16$ bytes in middle-endian.
Some of the bytes may contain ASCII control characters, including a NULL terminator, as well as values outside of the ASCII character range.

## Output Format
For each line, output each byte with the least significant bit first
in the same order it was received, followed by a newline character.

## Examples
Note: these are raw binary.
Depending on your browser/editor/terminal, copy/paste may not work.

TODO

## Historical Note
The PDP-11 uses middle-endian on 4-byte groups, so 'abcd' (little-endian within a byte)
is stored as 'cdab' (little-endian within a byte).
This is different from this problem, which is middle-endian within a byte.
However, it makes for a cool story, so I went with it.
