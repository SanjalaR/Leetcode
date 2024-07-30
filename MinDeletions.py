# Return the minimum number of deletions needed to make s balanced.
class Solution:
    def minimumDeletions(self, s: str) -> int:
        dele = 0
        bcount = 0
        for i in s:
            if i=='a':
                dele = min(dele+1, bcount)
            else:
                bcount+=1
        return dele
            
        
