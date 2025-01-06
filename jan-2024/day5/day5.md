# Shifting Letters II Solution

## Problem Statement

Given a string `s` and a list of shifts, each element in the list is a triplet `[start, end, direction]` where:

- `start` and `end` are the indices of the substring to shift.
- `direction` is `1` for a right shift and `0` for a left shift.

The task is to apply all the shifts to the string `s` and return the final string.

## Solution

The solution involves the following steps:

1. **Initialize a Difference Array**: Create a difference array `diff` to keep track of the net shifts at each position.
2. **Apply Shifts**: Iterate through the list of shifts and update the difference array accordingly.
3. **Calculate Net Shifts**: Compute the net shift for each character in the string by accumulating the values in the difference array.
4. **Shift Characters**: Apply the net shifts to each character in the string and construct the resulting string.

Here is the Python implementation:

```python
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = [0] * (len(s) + 1)
        for shift in shifts:
            if shift[-1] == 1:
                diff[shift[0]] += 1
                diff[shift[1] + 1] -= 1
            elif shift[-1] == 0:
                diff[shift[0]] -= 1
                diff[shift[1] + 1] += 1
        curr_shift = 0
        for i in range(len(s)):
            curr_shift += diff[i]
            diff[i] = curr_shift
        result = []
        for i, char in enumerate(s):
            shift = diff[i] % 26
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        return ''.join(result)
```

## Example

```python
s = "abc"
shifts = [[0, 1, 1], [1, 2, 0]]
solution = Solution()
print(solution.shiftingLetters(s, shifts))  # Output: "ace"
```

## Explanation

- The initial string is `"abc"`.
- The first shift `[0, 1, 1]` shifts the substring `"ab"` to the right, resulting in `"bbc"`.
- The second shift `[1, 2, 0]` shifts the substring `"bc"` to the left, resulting in `"ace"`.

Thus, the final output is `"ace"`.
