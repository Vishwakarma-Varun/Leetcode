class Solution:
    def arrangeCoins(self, n: int) -> int:
        # if n == 1:
        #     return n
        step = 1
        while n >= step:
            n = n - step
            step += 1
        return step-1

        