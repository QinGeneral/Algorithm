package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

class Solution200 {

  public static void main(String[] args) {
    // String[] strs = new String[] { "ab", "c" };
    String[] strs = new String[] { "eat", "tea", "tan", "ate", "nat", "bat" };
    System.out.println(new Solution200().groupAnagrams(strs));
  }

  public List<List<String>> groupAnagrams(String[] strs) {
    HashMap<String, List<String>> map = new HashMap<>();
    for (int i = 0; i < strs.length; i++) {
      String value = getStrValue2(strs[i]);
      System.out.println(value);
      if (map.containsKey(value)) {
        map.get(value).add(strs[i]);
      } else {
        List<String> tmp = new ArrayList<>();
        tmp.add(strs[i]);
        map.put(value, tmp);
      }
    }
    return new ArrayList<List<String>>(map.values());
  }

  private String getStrValue2(String str) {
    int[] arr = new int[26];
    for (int i = 0; i < str.length(); i++) {
      arr[str.charAt(i) - 'a']++;
    }
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] != 0) {
        sb.append((char) ('a' + i));
        sb.append(arr[i]);
      }
    }
    return sb.toString();
  }

  private String getStrValue(String str) {
    char[] chars = str.toCharArray();
    Arrays.sort(chars);
    return new String(chars);
  }
}
