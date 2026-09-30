class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        container = 0
        for i in range(1,n*n + 1):
            if w*i <= maxWeight:
                container += 1
        return container