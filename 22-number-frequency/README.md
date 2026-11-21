# Day 022 — Count Number Frequency

## Problem
Given a predefined list of numbers, count how many times each number appears using a dictionary.

## My Approach
I created an empty dictionary and looped through the numbers. If a number already existed as a dictionary key, I increased its value by one. Otherwise, I added it with an initial value of one.

## Concepts Learned
- Python dictionaries
- Dictionary keys and values
- Membership operator (`in`)
- Updating dictionary values
- Dictionary iteration
- Frequency counting

## Example
**Input**
```python
[4, 7, 2, 4, 9, 7, 4, 5, 7, 7]
```

**Output**
```text
4 found 3 times
7 found 4 times
2 found 1 times
9 found 1 times
5 found 1 times
```

## Complexity
- Time: O(n) average case
- Extra space: O(k), where k is the number of distinct numbers.

## What I Learned
A dictionary can efficiently track how frequently each value occurs. Each unique number becomes a key, and its frequency becomes the associated value.


## Possible Improvement
Use the `.items()` method to access dictionary keys and values together. Use the frequency values to display only duplicates.
