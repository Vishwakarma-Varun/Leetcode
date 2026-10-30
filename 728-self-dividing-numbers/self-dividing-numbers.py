class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ans = []
        for i in range(left,right+1):
            if i < 10:
                ans.append(i)
            elif "0" not in str(i):
                if all( i % int(j) == 0 for j in str(i)):
                    ans.append(i)
        return ans
                