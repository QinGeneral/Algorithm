import java.util.HashMap;
import java.util.Stack;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> charPos = new HashMap<>();
        int i = 0;
        int count = 0;
        int max = 0;
        while(i < s.length()) {
            Character str = s.charAt(i);
            if (charPos.get(str) == null) {
                charPos.put(str, i);
                count++;
                max = count > max ? count : max;
                i++;
            } else {
                count = 0;
                i = charPos.get(str) + 1;
                charPos.clear();
            }
        }
        return max;
    }
}