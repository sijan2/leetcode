# Day 4 - Unique Length-3 Palindromic Subsequences

## Problem Description

Given a string `s`, find the number of unique palindromic subsequences of length 3. A subsequence is palindromic if it reads the same forwards and backwards, and the first and last characters must be the same.

## Key Concepts

1. **Frequency Map**:

   - Store indices of each character in the string.
   - Use a dictionary to map characters to their indices.

2. **Set for Unique Subsequences**:
   - Use a set to store unique palindromic subsequences.

## Solution Approach

1. **Store Indices**:

   - Iterate through the string and store the indices of each character in a dictionary.

2. **Check Middle Positions**:
   - For each character in the string (excluding the first and last), check if it can form a palindromic subsequence with any character that appears before and after it.
   - Add valid subsequences to the result set.

## Complexity

- **Time Complexity**: O(n) where n is the length of the string.
- **Space Complexity**: O(n) for storing the indices and the result set.

## Code Implementation

```python
# filepath: /Users/sijan/leetcode/jan-2024/day4/4-jan-1930.py
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        freq = {}
        res = set()
        # Store indices for each character
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = []
            freq[s[i]].append(i)

        # Check each middle position
        for i in range(1, len(s) - 1):
            for char, indices in freq.items():
                if indices[0] < i < indices[-1]:
                    res.add((char, s[i]))
        return len(res)
```
