# Day 006 — Count from 1 to N

## Problem

Write a Python program that takes a positive integer `N` from the user and prints every number from 1 to N.

## My Approach

I first check whether the entered number is positive.

If it is positive, I use a `for` loop with `range()` to print the numbers from 1 through N.

I use:

`range(1, P + 1)`

because the ending value of `range()` is excluded.

## Concepts

- `input()`
- `int()`
- `if/else`
- `for` loop
- `range()`
- Iteration

## Example

Input:

5

Output:

1
2
3
4
5

## Test Cases

| Input | Expected Output |
|---:|---|
| 5 | 1, 2, 3, 4, 5 |
| 3 | 1, 2, 3 |
| 1 | 1 |
| 10 | 1 through 10 |
| -2 | Error message |

## Complexity

Time: O(N)

Space: O(1)

## What I Learned

I learned how to use a `for` loop with `range()`.

I also learned that the ending value of `range()` is not included, so `P + 1` is needed when I want to include P.

## Mistake I Made

I initially tried to use C/Java-style loop syntax:

`for i = 1, i <= P, i++`

Python uses `for` with `range()` instead.

I also initially used `range(P)`, which starts at 0 and does not include P.

## Possible Improvement

The program could be extended to count backwards or print only even/odd numbers.
