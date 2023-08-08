package leetcode;

class Solution76 {
    public static void main(String[] args) {
        System.out.println(new Solution76().minWindow("DAOBECODEBANC", "ABC"));
        System.out.println(new Solution76().minWindow("a", "a"));
        System.out.println(new Solution76().minWindow("a", "aa"));
        System.out.println(new Solution76().minWindow("bdab", "ab"));
    }

    public String minWindow(String s, String t) {
        if (s.length() < t.length()) {
            return "";
        }
        String result = "";

        int[] targetCharCounts = new int[58];
        char[] tChars = t.toCharArray();

        int[] sourceCharCounts = new int[58];
        char[] sChars = s.toCharArray();
        for (int i = 0; i < tChars.length; i++) {
            targetCharCounts[tChars[i] - 'A']++;
            sourceCharCounts[sChars[i] - 'A']++;
        }

        int start = 0, end = tChars.length - 1;
        while (end < sChars.length) {
            start = removePrefix(sourceCharCounts, sChars, start, end, tChars);
            if (end - start + 1 >= tChars.length && isArrayContains(sourceCharCounts, targetCharCounts)) {
                if (result.equals("") || end - start + 1 < result.length()) {
                    result = s.substring(start, end + 1);
                }
                sourceCharCounts[sChars[start] - 'A']--;
                start++;
            } else {
                end++;
                if (end < sChars.length) {
                    sourceCharCounts[sChars[end] - 'A']++;
                }
            }
        }
        return result;
    }

    private int removePrefix(int[] sCharCounts, char[] sChars, int start, int end, char[] tChars) {
        int i = start;
        for (; i < end; i++) {
            for (int j = 0; j < tChars.length; j++) {
                if (sChars[i] == tChars[j]) {
                    return i;
                }
            }
            sCharCounts[sChars[i] - 'A']--;
        }
        return i;
    }

    private boolean isArrayContains(int[] s, int[] t) {
        for (int i = 0; i < t.length; i++) {
            if (s[i] < t[i]) {
                return false;
            }
        }
        return true;
    }
}