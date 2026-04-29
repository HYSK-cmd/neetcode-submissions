class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        x = 0
        for i in range(len(nums)):
            x = nums[i]
            if x not in seen:
                seen[target-nums[i]] = i
            else:
                return [seen[x], i]
            print(seen)
        return [1, 2]