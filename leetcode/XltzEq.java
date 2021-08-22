class Solution {
    public boolean isPalindrome(String s) {
        if (s == null || s.length() == 0) {
            return true;
        }
        int start = 0;
        int end = s.length() - 1;

        while (start < end) {
            if (!isAlphabeta(s.charAt(start))) {
                start++;
                continue;
            }
            if (!isAlphabeta(s.charAt(end))) {
                end--;
                continue;
            }
            if (getLowercase(s.charAt(start)) != getLowercase(s.charAt(end))) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
    int TO_LOWER_CASE = 'a' - 'A';
    public int getLowercase(char c) {
        if (c >= 'A' && c <= 'Z') {
            return c + TO_LOWER_CASE;
        } else {
            return c;
        }
    }
    public boolean isAlphabeta(char c) {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9');
    }
}