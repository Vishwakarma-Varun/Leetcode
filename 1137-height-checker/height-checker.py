class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        misMatch = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                misMatch += 1
        return misMatch