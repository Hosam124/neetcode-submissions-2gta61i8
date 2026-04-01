class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=r=0
        mx =1
        cnt =0
        mp=defaultdict(int)
        while r<len(s):
            if s[r] not in mp:
                cnt+=1
                mp[s[r]]+=1
                r+=1
            else:
                mx = max(mx,cnt)
                while l<=r and s[r] in mp:
                    mp.pop(s[l])
                    l+=1
                    cnt-=1
        mx = max(mx,cnt)
        return min(mx,len(s))
