class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occur = []
        for i in set(arr):
            occur.append(arr.count(i))
        return len(occur) == len(list(set(occur)))