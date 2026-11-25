# Day 023 – Find the Most Frequent Number

## Problem
Given a list of numbers, find the number that appears most frequently and display its frequency.

## Concepts Learned
- Python dictionaries
- Frequency counting
- Dictionary `.items()` method
- Key-value unpacking
- Running maximum
- Comparing values and updating variables

## Example

**Input:**
```python
[4, 7, 2, 4, 9, 7, 4, 5, 7, 7]
```

**Output:**
```text
Most frequent number is 7 and it was shown for 4 times.
```

## Approach
1. Create an empty dictionary.
2. Count the occurrences of each number.
3. Iterate through the dictionary using `.items()`.
4. Track the number with the highest frequency.
5. Print the number and its frequency.

## Complexity
- Time: O(n), where n is the number of elements.
- Space: O(k), where k is the number of distinct elements.

## Learning Day
Day 023
