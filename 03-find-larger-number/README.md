# Day 003 — Find the Larger Number

## Problem

Write a Python program that takes two numbers from the user and determines which number is larger.

If both numbers are equal, the program should indicate that they are equal.

## My Approach

I take two numbers as input and compare them using conditional statements.

- If A is greater than B, A is larger.
- If A is less than B, B is larger.
- Otherwise, both numbers are equal.

## Concepts

- `input()`
- `int()`
- Variables
- `if`
- `elif`
- `else`
- Comparison operators
- f-strings

## Example

Input:

10
5

Output:

10 is larger

## Test Cases

| First | Second | Expected Output |
|---:|---:|---|
| 10 | 5 | 10 is larger |
| 3 | 9 | 9 is larger |
| 7 | 7 | 7 = 7 |
| -2 | 5 | 5 is larger |
| -10 | -20 | -10 is larger |

## Complexity

Time: O(1)

Space: O(1)

## What I Learned

I learned how to compare two numbers using `>`, `<`, and `==` and handle three possible outcomes using `if`, `elif`, and `else`.

## Mistake I Made

I initially used incorrect capitalization such as `If`, `Print`, and `Elif`.

I also made a spelling mistake with `Prnint`.

## Possible Improvement

The program could be extended to compare more than two numbers.
