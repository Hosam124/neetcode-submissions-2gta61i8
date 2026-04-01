class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people  = sorted(people)
        l,r= 0, len(people)-1
        cnt = 0
        res_p =len(people)
        while l<r:
            total =people[l] + people[r]
            if total <= limit :
                cnt+=1
                l+=1
                r-=1
                res_p-=2
            else:
                cnt+=1
                r-=1
                res_p-=1
        cnt+=res_p
        return cnt
