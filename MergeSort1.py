# Merge nums1 and nums2 into a single array sorted in non-decreasing order
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in nums2:
            while nums1[j]<i and j<m:
                j+=1
            # j+=1
            nums1.insert(j, i)
            nums1.pop()
        nums1.sort()

        
