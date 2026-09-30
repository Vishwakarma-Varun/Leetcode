class Solution:
    def finalString(self, s: str) -> str:
        k = ""
        for i in s:
            if i == "i":
                k = k[::-1]
            else:
                k = k + i
        return k