class Solution:
    def maxProduct(self, words: list[str]) -> int:
        ans = 0
        for i in range(len(words)):
            if i != len(words)-1:
                for j in range(i+1,len(words)):
                    if set(words[i]) & set(words[j]) == set():
                        if ans < len(words[i])*len(words[j]):
                            ans = len(words[i])*len(words[j])
        return ans