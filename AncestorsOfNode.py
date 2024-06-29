# Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = [[] for _ in range(n)] 
        ans = [[] for _ in range(n)] 
        for i in edges:
            res[i[0]].append(i[1])
        for i in range(n):
            self.dfs(i, i, ans, res)
        return ans
    
    def dfs(self, x, curr, ans, res):
        for i in res[curr]:
            if not ans[i] or ans[i][-1]!=x:
                ans[i].append(x)
                self.dfs(x, i, ans, res)
