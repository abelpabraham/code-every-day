# Day 011 — Sum of Odd Numbers from 1 to N

## Problem

Take a positive integer N and calculate the sum of all odd numbers between 1 and N.

## Example

Input:
10

Output:
The sum of odd numbers from 1 to 10 is 25

Because:

1 + 3 + 5 + 7 + 9 = 25

## My Approach

I used `range()` with a step of 2 to directly generate odd numbers.

Starting from 1 and increasing by 2 generates:

1, 3, 5, 7, 9, ...

Each generated number is added to the total.

## Concepts Learned

- for loop
- range()
- range step
- accumulator
- `+=` operator

## Complexity

Time: O(N)

Space: O(1)

## What I Learned

I learned that I can use the step parameter of `range()` to directly generate only the numbers I need.

## Possible Improvement

The same problem could also be solved by looping through every number and checking whether `i % 2 != 0`.
