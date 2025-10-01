class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while numBottles >= numExchange:
            newBottles = numBottles // numExchange
            numBottles = newBottles + (numBottles % numExchange)
            total += newBottles
        return total


        