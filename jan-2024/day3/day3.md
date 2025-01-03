# Day 3 - Ways to Split Array

## Problem Description

Given an array of integers `nums`, count the number of ways to split the array into two non-empty parts such that the sum of the left part is greater than or equal to the sum of the right part.

## Key Concepts

1. **Prefix Sum**:

   - Calculate the total sum of the array.
   - Use a running total to keep track of the sum of the left part.

2. **Iterative Comparison**:
   - Iterate through the array, updating the left and right sums.
   - Compare the sums to determine valid splits.

## Solution Approach

1. **Initialize Variables**:

   - `prefix` to store the total sum of the array.
   - `left` to store the running total of the left part.
   - `res` to count the number of valid splits.

2. **Iterate and Compare**:
   - For each element in the array (except the last one), update the `prefix` and `left` sums.
   - If the `left` sum is greater than or equal to the `prefix` sum, increment the `res` counter.

## Complexity

- **Time Complexity**: O(n) where n is the length of `nums`.
- **Space Complexity**: O(1) as we are using a constant amount of extra space.

## Code Implementation

```python
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = sum(nums)
        left = 0
        res = 0
        for i in range(len(nums) - 1):
            prefix -= nums[i]
            left += nums[i]
            if left >= prefix:
                res += 1
        return res
```
