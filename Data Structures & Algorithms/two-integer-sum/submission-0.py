class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        ls =[]
        for index,i in enumerate(nums) :
            if target-i in mp :
                ls.append(mp[target-i])
                ls.append(index)
            else :
                mp[i]=index

        return ls