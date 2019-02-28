# Binary Bit Blast

Aliens are taking over the world! The invaders from the planet ⦲⦚⧐⧕⦩ (unpronouncable by humans) communicate solely in Binary, but the code hasn't been broken... Yet! However, Earth's best Mathematicians have noticed that the binary communications in a way follow a set of rules, where bits can flip states if there are multiple 1s.

## Bit Flipping Example in Binary

`abcd`

`1000`

`1000`

Each Column of the Binary Number has certain properties. For every 1 in a binary column, the overall state of the column will flip from a 0 to a 1. For instance, since the First Number is `1000` in Binary, the state of Column `a` will be `1`. Moving onto the next column, there is another `1000` in Binary, so the `a` column state will be flipped to a `0` from the previous state `1`.

## Another Bit Flipping Example in Binary

`abcd`

`0101`

`0110`

In this example, the first number is `0101`. The `b` and `d` columns will have a value of `1`, while `a` and `c` will still have `0`. The next number causes the `b` column to flip back to 0, and the `c` and `d` columns to still be or become `1`.

## Breaking the code

The best bet that the Mathematicians have currently is to take all of the binary transmissions that the aliens broadcast and use this binary flipping rule to find a single number to change, such that the end result of all of the numbers becomes `0`. Then the number to change and the new number will be broadcasted back to the aliens. So far, the attempts to communicate with them in this manner have been successful! Maybe Earth has a chance after all!

However, the Mathematicians have become increasingly fatigued from doing this back and forth communication manually, so they need some help.

## Input

For Ease of use to you, the bits will be provided in decimal form.

N -> Number of Entries

A1 -> First Number

A2 -> Next Number

...

AN -> Last Number

For any number of the array, you will be guaranteed to get a case where the result from the bit flipping is not already 0. Also numbers may be repeated in the code.

1 <= N <= 6535

1 <= AN <= 2147483647

## Output

You will give back the number to change, and the new value to change it to. This will then be automatically be broadcasted back to the aliens.

`AN B`

where `AN` is the number that is being changed, and `B` is the new number to replace it with.

## Example 1

### Input
```
5
1
2
3
4
5
```

### Output

`1 0`

### Explanation

The Following Array is given: `1 2 3 4 5`, which converts to the following Binary:

```
001
010
011
100
101
```

Using Our rules about binary flipping from before, we can see that the bits come out to be `001`. Thus, we can change the `001` column to be `000`, satisfying the requirement that the end result of the bit flipping must become `000`.

## Example 2

### Input
```
6
1
2
3
4
5
6
```

### Output

`4 3`

### Explanation

The Array `1 2 3 4 5 6` is given. Here is the Binary:

```
001
010
011
100
101
110
```

Which gives `111` as the post-flipped state. Thus we must figure out how to remove from one of the binary numbers such that we get all 0s. This is done by changing `100` or `4` to be `011` or `3`

