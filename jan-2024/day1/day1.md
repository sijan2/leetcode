# Day 1 - Maximum Score from Splitting a String

## 1. Problem Statement

Given a binary string `s`, split it into two **non-empty** parts such that:

- The **number of `0`s** in the **left** part, plus
- The **number of `1`s** in the **right** part

is **maximized**.

### Example

- `s = "0110111"`
  Possible splits:
  1. **Left:** `"0"` | **Right:** `"110111"`
     - Zeros (left) = 1
     - Ones (right) = 4
     - **Score** = 1 + 4 = 5
  2. **Left:** `"01"` | **Right:** `"10111"`
     - Zeros (left) = 1
     - Ones (right) = 4
     - **Score** = 1 + 4 = 5
  - … and so on. In some splits, you might reach a **score** of 6.

## 2. Intuition

1. You consider each possible split index `i` where the string is divided into `s[:i]` (left) and `s[i:]` (right).
2. Count how many `0`s are in the **left** portion.
3. Count how many `1`s are in the **right** portion.
4. Keep track of the maximum sum (score) encountered.

## 3. Approach

1. **Brute Force / Naive**:

   - Loop over every possible split index from `1` to `len(s) - 1`.
   - For each split:
     - Count the number of `0`s in the left substring.
     - Count the number of `1`s in the right substring.
     - Update `max_score` accordingly.
   - **Time Complexity**: O(n²) (counting at each split)
   - **Space Complexity**: O(1)

2. **Optimized Approach (Prefix/Suffix arrays)**:
   - Precompute:
     - `prefix_zeros[i]`: number of zeros from `s[0]` to `s[i]`.
     - `suffix_ones[i]`: number of ones from `s[i]` to `s[n-1]`.
   - Then for each split at index `i`:
     - Zeros = `prefix_zeros[i - 1]`
     - Ones = `suffix_ones[i]`
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(n) (for prefix/suffix arrays)

## 4. Detailed Solution

```python
class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0

        # Iterate over each possible split point
        for i in range(len(s)):
            left = s[:i+1]      # Left substring includes character at i
            right = s[i+1:]     # Right substring is everything after i

            # If right is empty, this is not a valid split (i == len(s)-1)
            if not right:
                return max_score

            # Count zeros in the left substring
            count_zero = 0
            for char in left:
                if char == "0":
                    count_zero += 1

            # Count ones in the right substring
            count_one = 0
            for char in right:
                if char == "1":
                    count_one += 1

            # Calculate the score for this split
            score = count_zero + count_one

            # Update max_score if higher
            max_score = max(max_score, score)

        return max_score
```
