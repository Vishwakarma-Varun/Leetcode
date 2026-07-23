class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") >=2:
            return False
        count = 0
        for i in s:
            if count < 3:
                if i == "L":
                    count += 1
                else : count = 0
        return count < 3
