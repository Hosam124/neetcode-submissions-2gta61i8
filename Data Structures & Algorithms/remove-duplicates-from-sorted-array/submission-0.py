class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = -1000
        cnt =0
        ind= 0
        while ind < len(nums):
            if nums[ind] == curr:
                nums.pop(ind)
            else:
                curr= nums[ind]
                ind+=1
                cnt+=1

        return cnt
                