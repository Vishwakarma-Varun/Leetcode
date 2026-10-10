class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if all(nums[i] >= nums[j]*2 for j in range(len(nums)) if i != j):
                return i     
        return -1 