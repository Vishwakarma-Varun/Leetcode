class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = nums[0]
        add = 0
        for i in nums:
            for j in str(i):
                add = add + int(j)
            if ans > add:
                ans = add
            add = 0
        return ans