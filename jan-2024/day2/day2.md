# Day 2 - Count Vowel Strings in Ranges

## Problem Description

Given an array of strings `words` and a 2D array `queries`, count the number of strings that:

- Begin and end with a vowel
- Are within the range specified by each query

## Key Concepts

1. **Vowel Checking**:

   - Check if the first and last characters of a string are vowels.
   - Use a set for O(1) lookups.

2. **Prefix Sum Array**:
   - Precompute cumulative counts of vowel strings.
   - Enables O(1) range queries.

## Solution Approach

1. **Precompute Vowel Strings**:

   - Iterate through `words` and count strings that start and end with vowels.
   - Maintain a running total and store it in a list `res`.

2. **Process Queries**:
   - For each query, use the precomputed list `res` to quickly find the count of vowel strings in the specified range.

## Complexity

- **Time Complexity**: O(n + q) where n is the length of `words` and q is the number of queries.
- **Space Complexity**: O(n) for storing the prefix sum array.

## Code Implementation

```python
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        total = 0
        res = []
        vowels = {"a", "e", "i", "o", "u"}
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                total += 1
            res.append(total)

        result = []
        for L, R in queries:
            result.append(res[R] - (res[L - 1] if L > 0 else 0))
        return result
```
