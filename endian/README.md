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
You may assume the input length in bits is a multiple of 8.

## Output Format
For each byte, output the same byte reordered as described above.

## Examples
Note: these are raw binary.
Depending on your browser/editor/terminal, copy/paste may not work.

### Example 1
Input:
&6F
Output:
abcd
Explanation:
&6F is ['0b00010110', '0b00100110', '0b00110110', '0b01000110'] in binary.
Since we know we want to go from DCBA to BADC, we change the byte order and get
['0b01100001', '0b01100010', '0b01100011', '00b1100100'],
which in ASCII is 'abcd'.

### Example 2
Input:
G??7
Output:
this
Explanation:
G??7 is 01000111 10000110 10010110 00110111 in binary.
We change the byte order and get
01110100 01101000 01101001 01110011, which in ASCII is 'this'.

## Hint
xxd -b is your friend.

## Historical Note
The PDP-11 uses middle-endian on 4-byte groups, so 'abcd' (little-endian within a byte)
is stored as 'cdab' (little-endian within a byte).
This is different from this problem, which is middle-endian within a byte.
However, it makes for a cool story, so I went with it.