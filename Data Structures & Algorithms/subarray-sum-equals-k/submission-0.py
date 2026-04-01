class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0]+=1
        prefix=0
        cnt=0
        for num in nums:
            prefix+=num
            if (prefix - k ) in mp:
                cnt+=mp[prefix-k]
            
            mp[prefix]+=1
        return cnt
                