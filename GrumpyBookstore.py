# Return the maximum number of customers that can be satisfied throughout the day.
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans = 0
        for i in range(len(customers)):
            if grumpy[i]==0:
                ans += customers[i]
        unsat = 0
        for i in range(minutes):
            if grumpy[i]==1:
                unsat += customers[i]
        maxx = unsat
        for i in range(minutes, len(customers)):
            if grumpy[i-minutes] == 1:
                unsat -= customers[i-minutes]
            if grumpy[i]==1:
                unsat += customers[i]
            maxx = max(maxx, unsat)
        return ans+maxx
