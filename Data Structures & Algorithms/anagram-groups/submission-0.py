class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp =defaultdict(list)
        for i in strs :
            key = "".join(sorted(i))
            mp[key].append(i)
        return list(mp.values())
