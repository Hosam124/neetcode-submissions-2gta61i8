class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1,cand2,cnt1,cnt2=None,None,0,0
        for num in nums:
            if num == cand1:
                cnt1+=1
            elif num == cand2:
                cnt2+=1
            elif cnt1 == 0:
                cand1 ,cnt1 = num,1
            elif cnt2 == 0:
                cand2 ,cnt2 = num,1
            else:
                cnt1-=1
                cnt2-=1
        ls = []
        for cand in [cand1,cand2]:
            if (cand!= None and nums.count(cand)) > len(nums)//3 :
                ls.append(cand)
        return ls