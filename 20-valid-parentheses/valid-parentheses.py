class Solution(object):
    def isValid(self, s):
        l = ["()","[]","{}"]
        while s !="":
            k = s
            for i in l :
                if i in s:
                    s = s.replace(i,"")
            if s == k :
                return False
                break
        if not s:
            return True
        else:
            return False
        