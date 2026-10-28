# Day 020 — Separate Even and Odd Numbers

## Problem
Accept N integers and separate them into two lists: even numbers and odd numbers.

## My Approach
I created two empty lists. I used a loop to accept each number and checked its remainder when divided by 2. If the remainder was zero, I appended the number to the even list; otherwise, I appended it to the odd list.

## Concepts Learned
- Python lists
- The `append()` method
- `if/else` conditions
- The modulo operator `%`
- Filtering values into separate categories

## Example
**Input numbers:** `4, 7, 2, 9, 6, 3`

**Output**
```text
Odd numbers:
7
9
3
Even numbers:
4
2
6
```

## Complexity
- Time: O(n)
- Extra space: O(n), because the numbers are stored in the even and odd lists.

## What I Learned
I can classify values while iterating through the inputs and immediately store each value in the appropriate list.

## Possible Improvement
Print the lists directly instead of printing each number on a separate line.
