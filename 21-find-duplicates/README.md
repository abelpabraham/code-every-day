# Day 021 — Find Duplicate Numbers

## Problem
Accept N numbers and identify all values that appear more than once. Display each duplicate only once.

## My Approach
I created two lists: one to store the original numbers and another to store duplicates. I used the `in` membership operator to check whether a number had already appeared and prevented repeated entries in the duplicate list.

## Concepts Learned
- Python lists
- Membership operator (`in`)
- Membership negation (`not in`)
- Duplicate detection
- Conditional statements
- `len()` function

## Example
**Input:** `4, 7, 2, 4, 9, 7, 5`

**Output**
```text
Duplicate numbers:
4
7
```

## Complexity
- Time: O(n²) in the worst case, due to list membership checks.
- Extra space: O(n), for storing original numbers and duplicates.

## What I Learned
The `in` operator checks whether an element exists in a list. Maintaining a separate duplicate list helps ensure each duplicate is reported only once.
## Possible Improvement
Use a cleaner conditional structure to avoid adding repeated values back into the original list. Explore Python sets for more efficient membership checking later.
