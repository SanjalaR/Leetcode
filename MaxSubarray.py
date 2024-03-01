# Given an integer array nums, find the subarray with the largest sum, and return its sum.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_sum = -1e8
        sum = 0
        for i in nums:
            sum+=i
            if sum>max_sum:
                max_sum = sum 
            if sum<0:
                sum = 0
        return max_sum
