import java.util.ArrayList;
import java.util.HashSet;

class Solution {
    public String[] permutation(String s) {
        char[] chs = s.toCharArray();
        permutation(chs, 0);
        String[] result = new String[res.size()];
        for (int i = 0; i < result.length; i++) {
            result[i] = res.get(i);
        }
        return result;
    }

    ArrayList<String> res = new ArrayList<>();

    public void permutation(char[] chArray, int beginIndex) {
        if (beginIndex == chArray.length) {
            String str = new String(chArray);
            if (!res.contains(str)) {
                res.add(str);
            }
        } else {
            HashSet<Character> set = new HashSet<>();
            for (int i = beginIndex; i < chArray.length; i++) {
                if (set.contains(chArray[i])) {
                    continue;
                }
                set.add(chArray[i]);
                char temp = chArray[i];
                chArray[i] = chArray[beginIndex];
                chArray[beginIndex] = temp;

                permutation(chArray, beginIndex + 1);

                temp = chArray[i];
                chArray[i] = chArray[beginIndex];
                chArray[beginIndex] = temp;
            }
        }
    }
}