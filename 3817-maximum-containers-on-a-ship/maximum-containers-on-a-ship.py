class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        if n*n <= maxWeight // w :
            return n*n
        else:
            return maxWeight // w