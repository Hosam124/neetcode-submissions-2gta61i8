class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for i in nums:
            mp[i]+=1
        sortedItems = sorted(mp.items(),key=lambda x: x[1] , reverse=True)
        return [ k for k,v in sortedItems[:k]]
        

        