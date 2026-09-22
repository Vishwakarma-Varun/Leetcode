class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        sepNums = []
        for i in nums:
            i = str(i)
            for j in i :
                sepNums.append(int(j))
        return sepNums