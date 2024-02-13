# Given an array nums of size n, return the majority element.
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
      
        for i in nums:
            if nums.count(i)>len(nums)/2:
                return i 
        return -1
