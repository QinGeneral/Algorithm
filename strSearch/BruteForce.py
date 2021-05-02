def bruteForce(mainStr, matchStr):
    for i in range(0, len(mainStr) - len(matchStr) + 1):
        isMatch = True
        for j in range(0, len(matchStr)):
            if matchStr[j] != mainStr[i + j]:
                isMatch = False
                break
        if isMatch:
            return True

    return False

print(bruteForce("abcdefg", "def"))
print(bruteForce("abcdefg", "dea"))
print(bruteForce("abcdefg", "abc"))
print(bruteForce("abcdefg", "abd"))
print(bruteForce("abcdefg", "fg"))
print(bruteForce("abcdefg", "fh"))