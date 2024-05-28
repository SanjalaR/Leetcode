# Given an array nums of distinct integers, return all the possible permutations. 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        perm = []
        for i in nums:
            l1 = self.permute([n for n in nums if n != i])
            for j in l1:
                j.append(i)
            perm.extend(l1)
        return perm
        
        
