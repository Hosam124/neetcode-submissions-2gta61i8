class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        mx=0
        # while l<r:
        #     total = (r-l)*min(heights[l],heights[r])
        #     mx = max(mx,total)
        #     l_side = (r-l-1)*min(heights[l+1],heights[r])
        #     r_side = (r-l-1)*min(heights[l],heights[r-1])
        #     if l_side > r_side :
        #         total = min(heights[l],heights[l+1])
        #         mx = max(mx,total)
        #         l+=1
        #     elif l_side < r_side :
        #         total = min(heights[r],heights[r-1])
        #         mx = max(mx,total)
        #         r-=1
        #     else:
        #         if heights[r] > heights[l] :
        #             total = min(heights[l],heights[l+1])
        #             mx = max(mx,total)
        #             l+=1
        #         else :
        #             total = min(heights[r],heights[r-1])
        #             mx = max(mx,total)
        #             r-=1
        # return mx
        while l<r:
            total = (r-l)*min(heights[l],heights[r])
            mx = max(mx,total)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return mx 

        

