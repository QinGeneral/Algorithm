class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        for i in range(0, len(s) - 1):
            if map[s[i]] >= map[s[i + 1]]:
                sum += map[s[i]]
            else:
                sum -= map[s[i]]
        sum += map[s[-1]]
        return sum
