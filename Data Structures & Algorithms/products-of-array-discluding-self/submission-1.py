class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix, suffix = 1, 1
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i] 
            res[n-i-1] *= suffix
            suffix *= nums[n-i-1]
        return res
