class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i = k
        while k in nums:
            k += i
        return k