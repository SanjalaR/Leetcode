class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dup = []
        for i in arr:
            if arr.count(i)==1:
                dup.append(i)
        if len(dup)<k:
            return ''
        return dup[k-1]
        
