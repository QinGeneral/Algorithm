/*
 * @lc app=leetcode.cn id=10 lang=java
 *
 * [10] 正则表达式匹配
 */

// @lc code=start
class Solution {
    public boolean isMatch(String s, String p) {
        char[] source = s.toCharArray();
        int sourceIndex = 0;

        char[] chs = p.toCharArray();
        char pre;
        for (int i = 0; i < chs.length; i++) {
            if (chs[i] == '.') {
                sourceIndex++;
                pre = chs[i];
            } else if (chs[i] == '*') {
                if (pre != '.') {
                    if (pre == source[sourceIndex]) {
                        sourceIndex++;
                    } else {

                    }
                } else {

                }
            } else {
                if (chs[i] != source[sourceIndex]) {
                    return false;
                }
                sourceIndex++;
                pre = chs[i];
            }
        }
        return true;
    }
}
// @lc code=end
