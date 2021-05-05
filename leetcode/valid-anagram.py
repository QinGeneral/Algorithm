class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chs = {}
        for i in s:
            if i in chs.keys():
                chs[i] += 1
            else:
                chs[i] = 1
        for i in t:
            if i not in chs.keys():
                return False
            else:
                chs[i] -= 1
        for i in chs.keys():
            if chs[i] != 0:
                return False
        return True