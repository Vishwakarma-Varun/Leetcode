class Solution:
    def reverseWords(self, s: str) -> str:
        reverse = []
        for i in s.split(" "):
            reverse.append(i[::-1])
        return " ".join(reverse)