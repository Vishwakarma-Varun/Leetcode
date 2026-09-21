class Solution:
    def totalMoney(self, n: int) -> int:
        money = 0
        j = 1
        start = 1
        for i in range(1,n+1):
            money += j
            j += 1
            if i%7 == 0:
                start += 1
                j = start
        return money
            