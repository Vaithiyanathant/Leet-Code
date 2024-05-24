class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = 0
        n2 = 0
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                n1+=1
        for j in range(len(nums2)):
            if nums2[j] in nums1:
                n2+=1
        return [n1,n2]
        