class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        def sos(ind, target):
            if target==0:
                ans.append(ds[:])
            for i in range(ind, len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                ds.append(candidates[i])
                sos(i+1, target-candidates[i])
                ds.pop()
        candidates.sort()
        sos(0, target)
        return ans
        
