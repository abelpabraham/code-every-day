# Day 019 — Count Numbers Above Average

## Problem
Accept N numbers, calculate their average, and count how many numbers are strictly greater than that average.

## My Approach
I stored the entered numbers in a list. I calculated the average using a separate function, then looped through the list again to collect numbers greater than the average.

## Concepts Learned
- Python lists
- Creating and calling functions
- The `append()` method
- The `sum()` and `len()` functions
- Two-pass processing
- Filtering and counting
- Handling empty lists

## Example
**Input numbers:** `10, 20, 30, 40`

**Output**
```text
Average of numbers = 25.0
There are 2 numbers larger than average.
30
40
```

## Complexity
- Time: O(n)
- Extra space: O(n), because the program stores the numbers and matching values in lists.

## What I Learned
A list allows me to reuse the original inputs in a second loop. I also learned that I can get the number of matching values using `len()`.

## Possible Improvement
Count matching values directly without creating a second list, if I only need the count.
