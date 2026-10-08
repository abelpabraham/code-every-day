# Day 012 — Count Numbers Greater Than 10

## Problem

Take a positive integer N and count how many numbers between 1 and N are greater than 10.

## Example

Input:
15

Output:
There are 5 numbers that are greater than 10.

The numbers are:

11, 12, 13, 14, 15

## My Approach

Instead of checking every number from 1 to N, I started the loop at 11 because 11 is the first number greater than 10.

Then I increased the counter for every number until N.

## Concepts Learned

- for loop
- range()
- counting
- comparison
- choosing a useful starting point for a loop
- `+=` operator

## Complexity

Time: O(N)

Space: O(1)

## What I Learned

I learned that sometimes I can design the loop so that it only processes values that satisfy the condition.

Instead of checking every number, I can start the loop at the first valid number.

## Possible Improvement

The problem can also be solved by looping from 1 to N and using an `if` condition to check whether each number is greater than 10.
