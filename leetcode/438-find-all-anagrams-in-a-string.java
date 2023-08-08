package leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Objects;

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();
        if (s.length() < p.length()) {
            return result;
        }

        HashMap<Character, Integer> map = new HashMap<>();
        for (char ch : p.toCharArray()) {
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }
        char[] chars = s.toCharArray();
        HashMap<Character, Integer> map1 = new HashMap<>();
        for (int i = 0; i < p.length(); i++) {
            char ch = chars[i];
            map1.put(ch, map1.getOrDefault(ch, 0) + 1);
        }
        int start = 0;
        int end = p.length() - 1;
        while (end < chars.length) {
            boolean isEqual = isMapEqual(map1, map);
            if (isEqual) {
                result.add(start);
                while (end + 1 < chars.length && chars[start] == chars[end + 1]) {
                    start++;
                    end++;
                    result.add(start);
                }
            }

            if (end == chars.length - 1) {
                break;
            }
            int count = map1.get(chars[start]);
            if (count == 1) {
                map1.remove(chars[start]);
            } else {
                map1.put(chars[start], count - 1);
            }

            map1.put(chars[end + 1], map1.getOrDefault(chars[end + 1], 0) + 1);
            start++;
            end++;
        }
        boolean isEqual = isMapEqual(map1, map);
        if (isEqual && !result.contains(start)) {
            result.add(start);
        }
        return result;
    }

    private boolean isMapEqual(HashMap<Character, Integer> map, HashMap<Character, Integer> map1) {
        if (map.size() == map1.size()) {
            boolean isEqual = true;
            for (char key : map.keySet()) {
                if (!Objects.equals(map.get(key), map1.get(key))) {
                    isEqual = false;
                    break;
                }
            }
            return isEqual;
        }
        return false;
    }
}