# Return the number of indices where heights[i] != expected[i].
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = sorted(heights)
        return len([i for i in range(len(heights)) if heights[i]!=exp[i]])
