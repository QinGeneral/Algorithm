class Solution2:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        word = ""
        for i in range(len(s) - 1, -1, -1):
            print(s[i], result)
            if s[i] == " ":
                if len(word) == 0:
                    continue
                else:
                    result += self.reverseString(word) + " "
                    word = ""
            else:
                word += s[i]
            
        print('/' + result + '/')
        if len(word) > 0:
            result += self.reverseString(word)
        if len(result) > 0 and result[-1] == " ":
            return result[: len(result) - 1]

        return result

    def reverseString(self, s: str) -> str:
        newS = ""
        for i in range(len(s) - 1, -1, -1):
            newS += s[i]
        return newS


print(Solution().reverseWords("the sky is blue"))
print("/" + Solution().reverseWords(" hello world ") + "/")