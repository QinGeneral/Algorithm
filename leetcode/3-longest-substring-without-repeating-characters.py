class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        curStr = ""
        chSet = set()
        for ch in s:
            if not curStr:
                chSet.add(ch)
                curStr += ch
            else:
                if ch not in chSet:
                    chSet.add(ch)
                    curStr += ch
                else:
                    maxLength = max(maxLength, len(curStr))
                    index = -1
                    chSet.clear()
                    for i in range(len(curStr) - 1, -1, -1):
                        chSet.add(curStr[i])
                        if curStr[i] == ch:
                            index = i
                            break
                    curStr = curStr[index + 1 :]
                    curStr += ch

        maxLength = max(maxLength, len(curStr))
        return maxLength


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans


print(Solution().lengthOfLongestSubstring("dvdf"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("aabaab!bb"))