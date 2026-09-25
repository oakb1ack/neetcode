class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        runningTotal = 0
        biggestDiffIndex = 0
        tank = 0

        for i in range(len(gas)):
            runningTotal += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                biggestDiffIndex = i + 1
        
        if runningTotal >= 0:
            return biggestDiffIndex
        return -1
            