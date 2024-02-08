class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list = []
        for i in nums:
            if i not in new_list:
                new_list.append(i)
        nums.clear()
        nums.extend(new_list)
        return len(nums)
