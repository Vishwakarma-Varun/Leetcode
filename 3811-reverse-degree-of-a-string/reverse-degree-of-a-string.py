class Solution:
    def reverseDegree(self, s: str) -> int:
        degree = 0
        alpha = ["z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"]
        for i in range(len(s)):
            degree = degree + (i+1)*(alpha.index(s[i])+1)
        return degree