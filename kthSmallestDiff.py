class Solution:
    def countPairs(self, nums, mid):
        count, j = 0, 0
        for i in range(len(nums)):
            while j < len(nums) and nums[j] - nums[i] <= mid:
                j += 1
            count += j - i - 1
        return count

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        
        while low < high:
            mid = (low + high) // 2
            if self.countPairs(nums, mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low
