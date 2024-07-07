# Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles-1)//(numExchange-1)
        
