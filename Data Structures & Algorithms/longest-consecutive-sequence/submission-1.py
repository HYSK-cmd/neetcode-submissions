class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        for x in s:
            if x - 1 not in s:
                y = x
                while y in s:
                    y += 1
                best = max(best, y-x)
        return best
        # d = {}
        # for i in range(len(nums)):
        #     d[nums[i]] = i
        # best = 0
        # for i in range(len(nums)):
        #     j = 1
        #     while nums[i]+j in d:
        #         j += 1
        #     if j > best:
        #         best = j
        # return best
