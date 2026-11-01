class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        ans = {}
        for i in range(len(nums)):
            if nums[i] in ans:
                if abs(i - ans[nums[i]]) <= k:
                    return True
                else:
                    ans[nums[i]] = i
            else:
                ans[nums[i]] = i
        return False