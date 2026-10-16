# Day 017 — Count Target Occurrences

## Problem
Count how many times a target number appears among a series of user-entered numbers.

## My Approach
I initialized a counter to zero and checked each entered number against the target. Whenever they matched, I increased the counter by one. After the loop, I displayed the total number of occurrences.

## Concepts Learned
- `for` loops
- Conditional statements
- Frequency counting
- Counter variables
- The `+=` assignment operator

## Example
**Input**
```text
How many numbers? 5
Target number: 4
Numbers: 4, 7, 4, 2, 4
```

**Output**
```text
Number of occurrences of 4: 3
```

## Complexity
- Time: O(n)
- Extra space: O(1)

## What I Learned
A counter can track the number of times a condition is satisfied. Unlike a Boolean variable, which records whether a match exists, a counter records the total number of matches.

## Mistake I Made
I initially used `t_count++`, which is not valid Python syntax. I corrected it to `t_count += 1`.

## Possible Improvement
Validate the number of inputs to ensure it is positive.
