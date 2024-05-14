class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in set(nums1+nums2):
            if i in nums1 and nums2:
                f1 = nums1.count(i)
                f2 = nums2.count(i)
                mini = min(f1,f2)
                if mini>0:
                    for j in range(mini):
                        res.append(int(i))
        return res


        