class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        maxWords = 0
        for i in sentences:
            if maxWords < len(i.split(" ")):
                maxWords = len(i.split(" "))
        return maxWords