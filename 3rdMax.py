# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maximum = max(nums)
        nums[:] = [i for i in nums if i!=maximum]
        nums[:] = [i for i in nums if i!=max(nums)]
        return max(nums) if nums else maximum
        
