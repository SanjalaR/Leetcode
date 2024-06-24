# Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        flip = 0 
        isFlipped = [0]*n
        for i in range(n):
            if i>=k:
                flip ^= isFlipped[i-k]
            if nums[i] == flip:
                if i+k>n:
                    return -1
                ans +=1
                flip ^= 1
                if i+k<n:
                    isFlipped[i] = 1
        return ans
