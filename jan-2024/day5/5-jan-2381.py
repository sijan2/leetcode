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
