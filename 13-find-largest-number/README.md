# Day 013 — Find the Largest Number

## Problem

Ask the user how many numbers they want to enter. Read those numbers and find the largest one.

## Example

Input:
```text
How many numbers? 4
Enter number 1: 12
Enter number 2: 7
Enter number 3: 25
Enter number 4: 9
```

Output:
```text
The largest number is 25.
```

## My Approach

1. Read the number of inputs.
2. Read the first number and initialize `check` with it.
3. Loop through the remaining numbers.
4. Compare each number with `check`.
5. Update `check` when a larger number is found.
6. Print the largest number.

## Concepts Learned

- `for` loops
- `range()`
- comparison operators
- updating variables
- running maximum
- handling negative numbers

## Complexity

- Time: O(N)
- Auxiliary space: O(1)

## What I Learned

I learned how to find the largest number without storing every input. A variable can keep track of the largest value found so far.

## Possible Improvement

Add input validation to ensure the number of inputs is at least 1.
