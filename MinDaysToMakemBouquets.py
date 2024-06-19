# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        
        def f(d):
            l, bou = 0,0
            i = 0
            while i<len(bloomDay):
                while i<len(bloomDay) and bloomDay[i]<=d:
                    l+=1
                    if l==k:
                        bou+=1
                        l=0
                    i+=1
                if i<len(bloomDay) and bloomDay[i]>d:
                    l=0
                if bou>m:
                    return True
                i+=1
            return bou>=m
        
        l,r = min(bloomDay), max(bloomDay)
        while l<r:
            mid = l + (r-l) //2
            if f(mid):
                r = mid
            else:
                l = mid+1
        return l
