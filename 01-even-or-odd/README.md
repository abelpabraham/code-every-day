# Day 001 — Even or Odd

## Problem

Write a Python program that takes an integer from the user and determines whether it is even or odd.

## My Approach

I use the modulo operator `%` to find the remainder when the number is divided by 2.

- Remainder `0` → Even
- Otherwise → Odd

## Concepts

- `input()`
- `int()`
- `%` modulo operator
- `if/else`
- f-strings

## Example

Input:
10

Output:
10 is even

## Complexity

Time: O(1)

Space: O(1)

## What I Learned

The `%` operator gives the remainder of a division. I can use `number % 2` to determine whether a number is even or odd.

## Mistake I Made

I initially used incorrect Python capitalization and syntax such as `If` and `Print`. Python uses lowercase `if` and `print()`.

## Possible Improvement

Allow the program to repeatedly check numbers until the user chooses to exit.
