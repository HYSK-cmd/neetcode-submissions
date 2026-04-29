class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i

        best = 0
        for i in range(len(nums)):
            j = 1
            while nums[i]+j in d:
                j += 1
            if j > best:
                best = j
        return best
