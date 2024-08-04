class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        new_arr = []
        for i in range(len(nums)):
            new_arr.append(nums[i])
            summ = nums[i]
            for j in range(i+1, len(nums)):
                summ+=nums[j]
                new_arr.append(summ)
        new_arr.sort()
        mod = 10**9+7
        return sum(new_arr[left-1:right]) % mod

        
