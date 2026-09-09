class Solution:
    def countCommas(self, n: int) -> int:
        if n > 999 and n < 10**6 :
            return n-999
        elif n > (10**6 - 1) and n < 10**9:
            return (n-(10**6-1))*2 + 999*10**3  
        elif n > (10**9 - 1) and n < 10**12 :
            return (n-(10**9 - 1))*3 + 999*10**3 + 999*10**6*2
        elif n > (10**12 - 1) and n < 10**15:
            return (n - (10**12 - 1))*4 + 999000+999*10**6*2 + 999*10**9*3
        elif n == 10**15:
            return 999000 + 999*10**6*2 + 999*10**9*3 + 999*10**12*4 + 5
        return 0
        
        