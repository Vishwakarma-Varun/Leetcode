class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        substring = s[:k]
        s = s.replace(substring,substring[::-1],1)
        return s