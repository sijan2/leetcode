class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        freq = { }
        res = set()
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = []
            freq[s[i]].append(i)
        
        for i in range(1, len(s) - 1):
            for char, indices in freq.items():
                if indices[0] < i < indices[-1]:
                    res.add((char, s[i]))
        return len(res)
