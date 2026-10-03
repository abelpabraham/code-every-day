# Day 009 — Count Odd Numbers from 1 to N

## Problem

Take a positive integer N and count how many odd numbers exist between 1 and N.

## Example

Input:
10

Output:
No. of odd numbers from 1 - 10 is 5

The odd numbers are:
1, 3, 5, 7, 9

## My Approach

I used `range()` with a step of 2.

Starting from 1 and increasing by 2 generates only odd numbers:

1, 3, 5, 7, 9, ...

I then increased the counter once for every number generated.

## Concepts Learned

- for loop
- range()
- range step
- counting with a counter
- odd numbers

## Complexity

Time: O(N)

Space: O(1)

## What I Learned

I learned that `range()` can use a third argument called `step`.

Using a step of 2 allows me to directly generate odd numbers instead of checking every number.

## Mistake I Made

No major logic mistake. I found an alternative approach using the step parameter of `range()`.

## Possible Improvement

The variable name `Total` could be written as `total` to follow the usual Python naming convention.
