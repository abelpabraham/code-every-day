# Day 014 — Find the Smallest Number

## Problem

Ask the user how many numbers they want to enter. Read those numbers and find the smallest one.

## Example

Input:
```text
How many numbers? 4
Enter number 1: 12
Enter number 2: 7
Enter number 3: 25
Enter number 4: 3
```

Output:
```text
The smallest number is 3.
```

## My Approach

1. Read the number of inputs.
2. Read the first number and initialize `smallest` with it.
3. Loop through the remaining numbers.
4. Compare each new number with `smallest`.
5. Update `smallest` if the new number is smaller.
6. Print the final minimum.

## Concepts Learned

- `for` loops
- `range()`
- comparison operators
- conditional updates
- running minimum
- input validation

## Complexity

- Time: O(N)
- Auxiliary space: O(1)

## What I Learned

I learned how to find the smallest number by remembering the minimum value found so far and updating it when a smaller number appears.

## Possible Improvement

Use descriptive variable names such as `number` instead of `n1` to improve readability.
