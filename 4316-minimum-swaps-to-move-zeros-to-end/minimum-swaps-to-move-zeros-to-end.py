class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)) :
            if nums[i] == 0:
                for j in range(len(nums)):
                    if i < (len(nums))-(j+1):
                        if nums[(len(nums))-(j+1)] != 0:
                            nums[i] = nums[(len(nums))-(j+1)]
                            nums[(len(nums))-(j+1)] = 0
                            count += 1
                            break 
        return count