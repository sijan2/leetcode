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
