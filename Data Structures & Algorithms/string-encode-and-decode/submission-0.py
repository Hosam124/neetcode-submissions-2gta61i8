class Solution:

    def encode(self, strs: List[str]) -> str:
        st=""
        for i in strs:
            st+=str(len(i)) +"#"+i
            
        return st

    def decode(self, s: str) -> List[str]:
        ls = []
        i = 0
        while i < len(s):
            j=i
            while s[j] != '#':
                j+=1
            lenth= int(s[i:j])
            word= s[j+1:j+1+lenth]
            ls.append(word)
            i= j+1+lenth
        return ls

