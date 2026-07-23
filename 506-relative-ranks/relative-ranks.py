class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        b = sorted(score)[::-1]
        c = []
        for i in score:
            if b.index(i) == 0:
                c.append("Gold Medal")
            elif b.index(i) == 1:
                c.append("Silver Medal")
            elif b.index(i) == 2:
                c.append("Bronze Medal")
            else:
                c.append(f"{b.index(i)+1}")
        return c