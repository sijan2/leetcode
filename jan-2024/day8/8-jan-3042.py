class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            if len(str1) > len(str2):
                return False
            return str1 == str2[:len(str1)] and str1 == str2[-len(str1):]
            
        res = 0

        for i in range(len(words)):
            for j in range(1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]) == True and i < j:
                    res += 1
        return res

        
