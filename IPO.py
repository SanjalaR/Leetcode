# Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(capital, profits))
        projects.sort()
        maxHeap = []
        j = 0
        for i in range(k):
            while j<len(profits) and projects[j][0]<=w:
                heappush(maxHeap, -projects[j][1])
                j+=1
            if not maxHeap:
                break
            w+= -heappop(maxHeap)
        return w
