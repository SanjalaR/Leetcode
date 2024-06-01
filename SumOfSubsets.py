# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(k, target, path):
            if target==0:
                result.append(path)
                return
            if target<0:
                return
            for i in range(k, len(candidates)):
                backtrack(i, target-candidates[i], path+[candidates[i]])
        result = []
        candidates.sort()
        backtrack(0, target, [])
        return result
