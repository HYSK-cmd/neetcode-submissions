class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for x in range(len(nums)-2):
            i, j, k = x, x+1, len(nums)-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s==0: 
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
                    k-=1
                    j+=1
                    continue
                if s<0: j+=1
                if s>0: k-=1
        return res


            