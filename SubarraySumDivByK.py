# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_map = {0: 1} 
        cumulative_sum = 0
        count = 0 
        for i in range(len(nums)):
            cumulative_sum += nums[i]
            remainder = cumulative_sum % k
            if remainder<0:
                remainder+=k
            if remainder in remainder_map:
                count+=remainder_map[remainder]
                remainder_map[remainder]+=1
            else:
                remainder_map[remainder] = 1
        
        return count
            
