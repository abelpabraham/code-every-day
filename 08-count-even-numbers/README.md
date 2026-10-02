# Day 008 — Count Even Numbers from 1 to N

## Problem

Take a positive integer N and count how many even numbers exist between 1 and N.

## Example

Input:
10

Output:
No. of even numbers from 1 - 10 is 5

The even numbers are:
2, 4, 6, 8, 10

## My Approach

1. Take a number N as input.
2. Start a counter at 0.
3. Loop from 1 to N.
4. Check whether each number is even using `% 2`.
5. If the remainder is 0, increase the counter.
6. Print the final count.

## Concepts Learned

- for loop
- range()
- modulo operator `%`
- if condition
- counting with an accumulator
- comparison operator `==`

## Complexity

Time: O(N)

Space: O(1)

## What I Learned

I learned how to combine a loop, a condition, and a counter to count only the values that satisfy a condition.

## Mistake I Made

Initially, I increased the counter for every number in the loop. I learned that the counter must be increased only when the number satisfies the condition.

## Possible Improvement

The remainder can be checked directly using:

`if i % 2 == 0:`
