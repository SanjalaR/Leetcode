# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                sum = nums[i]+nums[j]+nums[k]
                if sum>0:
                    k-=1
                elif sum<0:
                    j+=1
                else:
                    ret.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
        return ret
            
