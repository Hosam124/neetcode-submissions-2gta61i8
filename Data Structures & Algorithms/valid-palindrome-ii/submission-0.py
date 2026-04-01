class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        while l<r :
            while r>l and not s[r].isalnum():
                r-=1
            while l<r and not s[l].isalnum():
                l+=1
            
            if s[l]!=s[r]:
                flage1=flage2=False
                l1,r1=l,r-1
                while l1<r1 :
                    while r1>l1 and not s[r1].isalnum():
                        r1-=1
                    while l1<r1 and not s[l1].isalnum():
                        l1+=1
                    if s[l1]!=s[r1]:
                        flage1 =True
                        break
                    l1+=1
                    r1-=1
                l2,r2=l+1,r
                while l2<r2 :
                    while r2>l2 and not s[r2].isalnum():
                        r2-=1
                    while l2<r2 and not s[l2].isalnum():
                        l2+=1
                    if s[l2]!=s[r2]:
                        flage2 =True
                        break
                    l2+=1
                    r2-=1
                if flage1 == flage2 and flage2==True:
                    return False
            l+=1
            r-=1
        return True
