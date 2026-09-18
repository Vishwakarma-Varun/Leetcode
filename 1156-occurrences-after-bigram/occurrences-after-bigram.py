class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        third = []
        words = text.split(" ")
        for i in range(len(words)):
            
            if words[i] == first:
                if i != len(words)-1:
                    if words[i+1] == second:
                        if i+1 != len(words)-1:
                            third.append(words[i+2])
        return third