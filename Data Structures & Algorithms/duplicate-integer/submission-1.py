class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       st = set(nums)
       if len(nums) > len(st) :
        return True
       else :
        return False