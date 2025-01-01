class Solution:
    def maxScore(self, s: str) -> int:
        left = ""
        right = ""
        max_score = 0
        for i in range(len(s)):
            score = 0
            left = s[:i+1]
            right = s[i+1:]
            count_zero = 0
            for zero in left:
                if zero == "0":
                    count_zero += 1
            count_one = 0
            if len(right) < 1:
                return max_score
            for one in right:
                if one == "1":
                    count_one += 1
            score = count_zero + count_one
            max_score = max(score, max_score)
        return max_score
