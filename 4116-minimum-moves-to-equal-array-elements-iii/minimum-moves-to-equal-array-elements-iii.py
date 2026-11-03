class Solution:
    def minMoves(self, nums: List[int]) -> int:
        moves = 0
        for i in nums:
            if i != max(nums):
                moves += max(nums) - i
        return moves