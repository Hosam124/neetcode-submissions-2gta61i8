class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = dict(Counter(nums))
        mx= 0
        for i in nums:
            cnt=0
            while i in mp:
                cnt+=1
                i-=1
            mx = max(mx,cnt) 
        return mx