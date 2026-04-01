class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ls=[]
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            l,r= i+1,len(nums)-1
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if total == 0:
                    ls.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l-1]==nums[l]:
                        l+=1
                    
                elif total < 0 :
                    l+=1
                else:
                    r-=1
        return ls