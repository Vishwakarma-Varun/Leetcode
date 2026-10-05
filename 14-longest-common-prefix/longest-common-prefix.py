class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = ""
        for i in range(len(strs[0])):
            if all( i < len(j) and strs[0][i] == j[i] for j in strs[1:]):
                ans += strs[0][i]
            else:
                break
        return ans
        