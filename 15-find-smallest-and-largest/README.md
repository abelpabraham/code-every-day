# Day 015 — Find the Smallest and Largest Numbers

## Problem

Read N numbers from the user and find both the smallest and largest values.

## Example

Input:
```text
How many numbers? 4
Enter number 1: 8
Enter number 2: 3
Enter number 3: 12
Enter number 4: 5
```

Output:
```text
Largest number: 12
Smallest number: 3
```

## My Approach

1. Read the number of inputs.
2. Use the first number to initialize both `smallest` and `largest`.
3. Loop through the remaining numbers.
4. Update `largest` if a number is greater than it.
5. Update `smallest` if a number is less than it.
6. Print both values.

## Concepts Learned

- For loops
- Comparison operators
- Conditional updates
- Running minimum
- Running maximum
- Tracking multiple values
- Input validation

## Complexity

- Time: O(N)
- Auxiliary space: O(1)

## What I Learned

I learned how to track the smallest and largest values simultaneously without storing all the inputs in a list.

## Possible Improvement

Use descriptive variable names and separate `if` statements to make the two comparisons clearer.
