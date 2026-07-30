class Solution:
    def maxProduct(self, n: int) -> int:
        l = []
        while n>0:
            l.append(n%10)
            n = n//10
        l.sort()
        l = l[::-1]
        return l[0]*l[1]