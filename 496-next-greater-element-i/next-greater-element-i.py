class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1 :
            if nums2.index(i) == len(nums2)-1:
                ans.append(-1)
            else:
                for j in range(nums2.index(i)+1,len(nums2)):
                    if i > nums2[j] and j != len(nums2)-1:
                        continue
                    elif i < nums2[j]:
                        ans.append(nums2[j])
                        break
                    else:
                        ans.append(-1)
                        break
        return ans