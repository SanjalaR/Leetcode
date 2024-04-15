# Write a function to find the longest common prefix string amongst an array of strings.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        strs = sorted(strs)
        print(strs)
        a = strs[0]
        b = strs[-1]
        for i in range(min(len(a), len(b))):
            if (a[i]!=b[i]):
                return res
            res+=a[i]
        return res
        
                    
