class Solution:
    def trap(self, height: List[int]) -> int:
        l,r  =0,1
        top = height[l]
        mx=0
        cnt=0
        while r<len(height):
            if top > height[r] :
                cnt+= height[r]
            else:
                mx += max((top*(r-l-1))-cnt,0)
                top = height[r]
                l = r
                cnt=0
            r+=1
        if l < len(height)-1:
            height.reverse()
            n = len(height)-l
            l,r  =0,1
            top = height[l]
            cnt=0
            while r<n:
                if top > height[r] :
                    cnt+= height[r]
                else:
                    mx += max((top*(r-l-1))-cnt,0)
                    top = height[r]
                    l = r
                    cnt=0
                r+=1


        return mx 
