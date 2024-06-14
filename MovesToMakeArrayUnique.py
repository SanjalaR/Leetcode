# Return the minimum number of moves to make every value in nums unique.
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        numTracker = 0
        moves = 0
        for i in nums:
            numTracker = max(i, numTracker)
            moves += numTracker-i
            numTracker+=1
        return moves
