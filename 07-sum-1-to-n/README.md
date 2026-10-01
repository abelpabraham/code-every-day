# Day 007 — Sum of Numbers from 1 to N

## Problem

Write a Python program that takes a positive integer N from the user and calculates the sum of all numbers from 1 to N.

## My Approach

I first check whether the input is positive.

Then I create a variable called `total` and start it at 0.

I use a `for` loop to go from 1 to N and add each number to `total`.

## Concepts

- `input()`
- `int()`
- `if/else`
- `for` loop
- `range()`
- Variables
- Accumulation
- Addition

## Example

Input:

5

Output:

Sum = 15

Because:

1 + 2 + 3 + 4 + 5 = 15

## Test Cases

| Input | Expected Output |
|---:|---:|
| 5 | Sum = 15 |
| 3 | Sum = 6 |
| 1 | Sum = 1 |
| 10 | Sum = 55 |
| 0 | Error message |

## Complexity

Time: O(N)

Space: O(1)

## What I Learned

I learned the accumulation pattern.

I start with:

`total = 0`

and repeatedly update it:

`total = total + i`

until all numbers from 1 to N have been processed.

## Mistake I Made

I initially printed `sum` instead of `total`.

I also experimented with calling the function recursively when the input was invalid, but recursion was not necessary for this problem.

## Possible Improvement

The program could be extended to calculate the sum of only even numbers or only odd numbers.
