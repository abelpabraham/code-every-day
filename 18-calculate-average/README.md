# Day 018 — Calculate the Average

## Problem
Accept a specified number of integers, calculate their sum, and find their average.

## My Approach
I asked the user how many numbers they wanted to enter. I used a loop to collect each number and add it to a running total. After the loop, I divided the total by the number of inputs.

## Concepts Learned
- `for` loops and `range()`
- Accumulation using `+=`
- Arithmetic mean (average)
- Input validation using `if/else`
- Avoiding unnecessary variables

## Example
**Input**
```text
How many numbers: 4
Enter number 1: 10
Enter number 2: 20
Enter number 3: 30
Enter number 4: 40
```

**Output**
```text
Average of entered numbers = 25.0
```

## Complexity
- Time: O(n)
- Extra space: O(1)

## What I Learned
The average is calculated after accumulating all the inputs. When the number of inputs is already known, I can use it directly instead of maintaining a separate counter.

## Possible Improvement
Handle non-integer inputs and invalid input counts more robustly.
