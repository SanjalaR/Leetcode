# Return the minimum number of operations needed to go back to the main folder after the change folder operations.
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for i in logs:
            if '.' not in i:
                count+=1
            if i=='../':
                count-=1
                if count<0:
                    count=0
        return count
        
