class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for i in nums:
            mp[i]+=1
        ls = [[] for _ in range(len(nums)+1)]
        for key,val in mp.items():
            ls[val].append(key)
        out =[]
        for i in range (len(nums),-1,-1):
            if len(ls[i])>0:
                while k>0 and len(ls[i])>0:
                    out.append(ls[i][-1])
                    ls[i].pop()
                    k-=1
            if k==0:
                return out
