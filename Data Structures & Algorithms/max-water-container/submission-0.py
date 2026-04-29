class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx=0
        i,j = 0, len(heights)-1
        while i<j:
            w,h = j-i, min(heights[i], heights[j])
            area=w*h
            if area>mx:
                mx=area
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return mx
                
               