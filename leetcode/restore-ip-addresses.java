class Solution {

    int SEG_COUNT = 4;
    int[] segments = new int[SEG_COUNT];
    ArrayList<String> ans = new ArrayList<>();
    public List<String> restoreIpAddresses(String s) {
        restore(s, 0, 0);
        return ans;
    }

    public void restore(String s, int segI, int strI) {
        if (segI == SEG_COUNT) {
            if (strI == s.length()) {
                StringBuilder temp = new StringBuilder();
                for (int i = 0; i < SEG_COUNT; i++) {
                    temp.append(segments[i]);
                    if (i != SEG_COUNT - 1) {
                        temp.append(".");
                    }
                }
                if (!ans.contains(temp.toString())) {
                    ans.add(temp.toString());
                }
            }
            return;
        }
        if (strI == s.length()) {
            return;
        }
        if (s.charAt(strI) == '0') {
            segments[segI] = 0;
            restore(s, segI + 1, strI + 1);
        }
        int addr = 0;
        for (int i = strI; i < s.length(); i++) {
            addr = addr * 10 + (s.charAt(i) - '0');
            if (addr > 0 && addr <= 255) {
                segments[segI] = addr;
                restore(s, segI + 1, i + 1);
            } else {
                break;
            }
        }
    }
}