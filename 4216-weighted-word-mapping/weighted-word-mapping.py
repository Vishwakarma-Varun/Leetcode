class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        ans = ""
        sum = 0
        for i in words:
            for j in i:
                sum = sum + weights[alpha.index(j)]
            sum = sum % 26
            ans = ans + alpha[25- sum]
            sum = 0
        return ans