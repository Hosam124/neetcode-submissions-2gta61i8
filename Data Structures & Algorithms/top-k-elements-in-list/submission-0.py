class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for i in nums :
            mp[i]+=1
        sorted_items = sorted(mp.items(),key= lambda item : item[1] , reverse=True)
        return [key for key,_ in sorted_items[:k]]
        

        