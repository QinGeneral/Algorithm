class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        if (strs.length == 1) {
            return strs[0];
        }
        StringBuilder prefix = new StringBuilder();
        int index = 0;
        while (true) {
            String ch = null;
            boolean isMatch = true;
            for (int i = 0; i < strs.length; i++) {
                if (strs[i].length() > index) {
                    String cur = strs[i].charAt(index) + "";
                    if (ch == null) {
                        ch = cur;
                    } else {
                        if (!ch.equals(cur)) {
                            isMatch = false;
                            break;
                        } else {
                            continue;
                        }
                    }
                } else {
                    isMatch = false;
                    break;
                }
            }
            if (isMatch) {
                prefix.append(ch);
                index++;
            } else {
                break;
            }
        }
        return prefix.toString();
    }
}

class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        if (strs.length == 1) {
            return strs[0];
        }
        String prefix = strs[0];
        for (int i = 1; i < strs.length; i++) {
            prefix = longestCommonPrefix(prefix, strs[i]);
            if (prefix.length() == 0) {
                break;
            }
        }
        return prefix;
    }

    public String longestCommonPrefix(String str1, String str2) {
        int index = 0;
        while (str1.length() > index && str2.length() > index) {
            if (str1.charAt(index) == str2.charAt(index)) {
                index++;
                continue;
            } else {
                break;
            }
        }
        return str1.substring(0, index);
    }
}