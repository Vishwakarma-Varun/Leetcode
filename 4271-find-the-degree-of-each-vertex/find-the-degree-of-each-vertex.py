class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        for i in matrix:
            ans.append(i.count(1))
        return ans