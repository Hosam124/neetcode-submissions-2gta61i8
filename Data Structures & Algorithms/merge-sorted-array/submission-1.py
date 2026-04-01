class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1=p2=0
        while p1<len(nums1):
            if p2 <len(nums2) and nums1[p1]>=nums2[p2]  :
                nums1.insert(p1,nums2[p2])
                p2+=1
                nums1.pop()
            if p1 == len(nums1)-1 and p2<len(nums2):
                
                for _ in range(len(nums2)-p2):
                    nums1.pop()
                while p2<len(nums2):
                    nums1.append(nums2[p2])
                    p2+=1
            
            p1+=1
            
        