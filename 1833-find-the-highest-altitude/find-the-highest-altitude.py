class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        point = 0
        altitude = [0]
        for i in gain:
            point = point + i
            altitude.append(point)
        return max(altitude)