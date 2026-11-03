class Solution:
    def minMoves(self, nums: List[int]) -> int:
        moves = 0
        big = max(nums)
        for i in nums:
            if i != big:
                moves += big - i
        return moves