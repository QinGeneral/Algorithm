class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] s1Hash = new int[26];
        getFrequence(s1, s1Hash);
        int[] s2Hash = new int[26];
        for (int i = 0;i <= (s2.length() - s1.length()); i++) {
            getFrequence(s2.substring(i, s1.length() + i), s2Hash);
            if (isEqual(s1Hash, s2Hash)) {
                return true;
            }
        }
        return false;
    }

    public boolean isEqual(int[] array1, int[] array2) {
        for (int i = 0; i < array1.length; i++) {
            if (array1[i] != array2[i]) {
                return false;
            }
        }
        return true;
    }
    public void getFrequence(String str, int[] result) {
        for (int i = 0; i < result.length; i++) {
            result[i] = 0;
        }
        for (int i = 0; i < str.length(); i++) {
            int index = str.charAt(i) - 'a';
            result[index]++;
        }
    }
}

class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s2.length() < s1.length()) {
            return false;
        }
        int[] s1Hash = new int[26];
        getFrequence(s1, s1Hash);
        int[] s2Hash = new int[26];
        getFrequence(s2.substring(0, s1.length()), s2Hash);
        if (Arrays.equals(s1Hash, s2Hash)) {
            return true;
        }
        for (int i = 0;i < (s2.length() - s1.length()); i++) {
            s2Hash[s2.charAt(i) - 'a']--;
            s2Hash[s2.charAt(i + s1.length()) - 'a']++;
            if (Arrays.equals(s1Hash, s2Hash)) {
                return true;
            }
        }
        return false;
    }
    public void getFrequence(String str, int[] result) {
        for (int i = 0; i < result.length; i++) {
            result[i] = 0;
        }
        for (int i = 0; i < str.length(); i++) {
            int index = str.charAt(i) - 'a';
            result[index]++;
        }
    }
}