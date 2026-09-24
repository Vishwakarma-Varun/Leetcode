class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            for j in str(nums[i]):
                sum += int(j)
            if sum == i:
                return i
            sum = 0
        return -1