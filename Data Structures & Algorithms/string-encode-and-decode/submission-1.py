class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=str(len(i))+"#"+i
        return s

    def decode(self, s: str) -> List[str]:
        ls =[]
        j=0
        while j<len(s):
            num=""
            while s[j] !='#':
                num+=s[j]
                j+=1
            int_num= int(num)
            st = s[j+1:j+int_num+1]
            ls.append(st)
            j+=int_num+1
        return ls
        
