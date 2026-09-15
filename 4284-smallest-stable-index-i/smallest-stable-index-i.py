class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        i = 0
        score = -1
        while i < len(nums):
            score = max(nums[:i+1]) - min(nums[i:])
            if score <= k:
                return i
            i += 1
        else:
            return -1