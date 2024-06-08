# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1} 
        cumulative_sum = 0
        
        for i in range(len(nums)):
            cumulative_sum += nums[i]
            remainder = cumulative_sum % k
            
            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1: 
                    return True
            else:
                remainder_map[remainder] = i
        
        return False
