class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=str(len(i))+"#"+i
        return s

    def decode(self, s: str) -> List[str]:
        ls = []
        ind=0
        while ind<len(s):
            n = ""
            while s[ind]>='0' and s[ind]<='9':
                n+=s[ind]
                ind+=1
            n = int(n)
            ls.append(s[ind+1:ind+n+1])
            ind+=n+1
        return ls 
        
