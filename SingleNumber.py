# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in range(len(nums)):
            if nums[num] not in nums[num+1:] and nums[num] not in nums[:num]:
                return nums[num]
