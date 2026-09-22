class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum = 0
        product = 1
        for i in str(n):
            sum += int(i)
            product *= int(i)
        return n % (sum + product) == 0
