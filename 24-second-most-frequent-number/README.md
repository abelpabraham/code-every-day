# Day 024 – Find the Second Most Frequent Number

## Problem
Given a list of numbers, find the second most frequent distinct number and its frequency without using sorting or `max()`.

## Concepts Learned
- Frequency dictionaries
- Dictionary `.items()`
- Key-value unpacking
- Running maximum
- Tracking first and second place
- Conditional updating

## Example

**Input:**
```python
[4, 7, 2, 4, 9, 7, 4, 5, 7, 7, 9, 9, 9]
```

**Output:**
```text
Second most frequent number: 9
Frequency: 4
```

## Approach
1. Build a dictionary to count each number.
2. Initialize first-place and second-place trackers.
3. Iterate through the frequency dictionary.
4. If a number beats first place, move the previous first place to second.
5. Otherwise, if it beats second place, update second place.
6. Print the second most frequent number and its frequency.

## Complexity
- Time: O(n), where n is the number of input elements.
- Space: O(k), where k is the number of distinct numbers.

## Learning Day
Day 024
