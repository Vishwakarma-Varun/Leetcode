class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        ans = []
        for i in set(nums):
            if nums.count(i) == 1:
                ans.append(i)
        return ans