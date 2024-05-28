# You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        for i in range(len(nums)+1):
            count = 0
            for j in nums:
                if j>=i:
                    count+=1
            if count == i:
                return i
        return -1
            
