# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        return [i for i in nums if nums.count(i)==1]
