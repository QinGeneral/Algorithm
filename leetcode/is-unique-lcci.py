class Solution:
    def isUnique(self, astr: str) -> bool:
        for i in range(0, len(astr)):
            for j in range(i + 1, len(astr)):
                if astr[i] == astr[j]:
                    return False
        
        return True