# Day 016 — Linear Search

## Problem

Read a positive number of inputs and determine whether a target number appears among them.

## Example

Input:
```text
How many numbers? 5
Enter number to search for: 25
Enter number 1: 12
Enter number 2: 7
Enter number 3: 25
Enter number 4: 3
Enter number 5: 9
```

Output:
```text
Number found!
```

## My Approach

1. Read the number of inputs.
2. Initialize `found` to `False`.
3. Read the target number.
4. Read each number and compare it with the target.
5. If a match is found, set `found` to `True`.
6. After the loop, print the search result.

## Concepts Learned

- `for` loops
- `range()`
- Boolean values (`True` and `False`)
- Assignment (`=`) versus equality comparison (`==`)
- Linear search
- Tracking a condition with a Boolean variable

## Complexity

- Time: O(N)
- Auxiliary space: O(1)

## What I Learned

I learned how to search for a target value by checking inputs one by one and tracking whether a match exists.

## Mistakes I Made

- Used lowercase Boolean values.
- Used `==` where assignment with `=` was required.
- Placed the not-found message inside the loop.

## Possible Improvement

Store the numbers in a list so the target can be entered after all the numbers, and stop searching as soon as a match is found.
