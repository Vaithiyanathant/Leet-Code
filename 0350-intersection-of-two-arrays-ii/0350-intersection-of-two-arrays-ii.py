class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        res = []
        for i in set(nums1):
            if i in d2 and d2[i] !=0:
                ma = min(d1[i],d2[i])
                res.extend([i]*ma)
        return res
        
        