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
