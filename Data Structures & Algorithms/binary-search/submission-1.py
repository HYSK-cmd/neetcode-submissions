class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binary_search(nums, target, 0, len(nums)-1)

def binary_search(nums, target, l, r) -> int:
    if l > r:
        return -1
    mid = (l + r) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        return binary_search(nums, target, mid + 1, r)
    else:
        return binary_search(nums, target, l, mid - 1)