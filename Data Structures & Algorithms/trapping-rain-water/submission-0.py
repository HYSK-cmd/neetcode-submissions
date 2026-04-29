class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len(height)-1
        mx_left, mx_right = height[l], height[r]
        res=0
        while l<r:
            if mx_left<mx_right:
                l+=1
                mx_left=max(mx_left, height[l])
                res+=mx_left-height[l]
            else:
                r-=1
                mx_right=max(mx_right, height[r])
                res+=mx_right-height[r]
        return res
            