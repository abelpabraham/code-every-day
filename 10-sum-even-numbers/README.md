# Day 010 — Sum of Even Numbers from 1 to N

## Problem

Take a positive integer N and calculate the sum of all even numbers between 1 and N.

## Example

Input:
10

Output:
Sum of even numbers between 1 and 10 is: 30

Because:

2 + 4 + 6 + 8 + 10 = 30

## My Approach

1. Take N as input.
2. Start the total at 0.
3. Loop from 1 to N.
4. Check whether each number is even using `% 2`.
5. If it is even, add it to the total.
6. Print the final sum.

## Concepts Learned

- for loop
- range()
- modulo operator `%`
- if condition
- accumulator
- `+=` operator

## Complexity

Time: O(N)

Space: O(1)

## What I Learned

I learned how to combine a condition with an accumulator.

I also used `total += i`, which is a shorter form of `total = total + i`.

## Possible Improvement

Instead of checking every number, `range()` can be used with a step of 2 to directly generate even numbers.
