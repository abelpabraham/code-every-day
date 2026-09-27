# Day 005 — Even or Odd Without Modulo

## Problem

Write a Python program that determines whether a number is even or odd without using the `%` operator.

## My Approach

I used floor division `//` and normal division `/`.

For an even number, dividing by 2 produces a whole number, so:

`n // 2 == n / 2`

For an odd number, normal division produces a decimal value, while floor division removes the decimal part.

## Concepts

- `input()`
- `int()`
- Functions
- Parameters
- `return`
- `//` floor division
- `/` normal division
- `if/else`

## Example

Input:

10

Output:

entered number is even

## Test Cases

| Input | Expected |
|---:|---|
| 10 | even |
| 7 | odd |
| 0 | even |
| -4 | even |
| -7 | odd |

## Complexity

Time: O(1)

Space: O(1)

## What I Learned

I learned that the same programming problem can sometimes be solved in different ways.

I also practiced creating a function and returning a result from it.

## Mistake I Made

I initially forgot a closing parenthesis in `input()` and used `If` instead of Python's lowercase `if`.

I also initially called the function without printing its returned result.

## Possible Improvement

A more direct approach for determining even or odd would be to use the modulo operator `%`.

This exercise intentionally avoided `%` to practice thinking about another solution.
