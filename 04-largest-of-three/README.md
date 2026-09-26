# Day 004 — Largest of Three Numbers

## Problem

Write a Python program that takes three different numbers from the user and determines which number is the largest.

## My Approach

I compare the first number with both other numbers.

If `a` is greater than both `b` and `c`, then `a` is the largest.

Otherwise, I check whether `b` is greater than `c`.

If neither condition is true, `c` must be the largest.

## Concepts

- `input()`
- `int()`
- Variables
- `if`
- `elif`
- `else`
- Comparison operators
- `and` operator

## Example

Input:

10
25
15

Output:

25 is larger.

## Test Cases

| A | B | C | Expected Output |
|---:|---:|---:|---|
| 10 | 20 | 5 | 20 is larger |
| 30 | 10 | 20 | 30 is larger |
| 5 | 8 | 15 | 15 is larger |
| -2 | -10 | -5 | -2 is larger |
| 100 | 50 | 75 | 100 is larger |

## Complexity

Time: O(1)

Space: O(1)

## What I Learned

I learned how to combine multiple conditions using the `and` operator.

For example:

`a > b and a > c`

means both conditions must be true.

## Mistake I Made

I initially used `&&` for combining conditions.

Python uses `and` instead of `&&`.

## Possible Improvement

The program could be modified to handle cases where two or all three numbers are equal.
