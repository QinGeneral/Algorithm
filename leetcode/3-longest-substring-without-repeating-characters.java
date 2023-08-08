package leetcode;

import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        char[] chars = s.toCharArray();
        int maxLength = 0;

        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < chars.length; i++) {
            if (!map.containsKey(chars[i])) {
                map.put(chars[i], i);
            } else {
                i = map.get(chars[i]);
                maxLength = Math.max(maxLength, map.size());
                System.out.println("max " + maxLength + " " + map.size());
                map.clear();
            }
        }
        maxLength = Math.max(maxLength, map.size());
        return maxLength;
    }
}