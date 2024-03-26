# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res= []
        for i in nums1:
            if i in nums2:
                res.append(i)
                nums2.remove(i)
        return res
