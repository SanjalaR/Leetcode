# Return the maximum profit we can achieve after assigning the workers to the jobs.
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        profs = sorted(zip(difficulty, profit))
        worker.sort()
        if worker[-1]<difficulty[0]:
            return 0
        result = 0
        best = 0
        j = 0
        for w in worker:
            while j<len(profs) and profs[j][0]<=w:
                best = max(best, profs[j][1])
                j+=1
            result += best
        return result
        
