class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            if n < 10:
                if n % t == 0:
                    return n
            else:
                if ((n%10)*(n//10)) % t == 0 :
                    return n
            n += 1