# Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        tot = customers[0][1]
        stack = customers[0][0]+customers[0][1]
        for i in range(1, len(customers)):
            start = max(stack, customers[i][0])
            end = start + customers[i][1]
            stack = end
            tot += end-customers[i][0]
        return tot/len(customers)
        
