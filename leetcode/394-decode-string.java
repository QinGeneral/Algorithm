package leetcode;

import java.util.LinkedList;

class Solution394 {
    public static void main(String[] args) {
        String s = "3[a21[c]2[de]]ab";
        System.out.println(new Solution394().decodeString(s));
    }

    public String decodeString(String s) {
        LinkedList<Integer> numberStack = new LinkedList<>();
        LinkedList<String> charStack = new LinkedList<>();

        StringBuilder result = new StringBuilder();
        StringBuilder num = new StringBuilder();

        int start = 0;
        char[] chars = s.toCharArray();
        while (start < chars.length) {
            char ch = chars[start];
            while (isNumber(ch)) {
                num.append(ch);
                start++;
                ch = chars[start];
            }

            int number = 1;
            if (num.length() > 0) {
                number = Integer.parseInt(num.toString());
                num = new StringBuilder();
                System.out.println(number);
            }
            numberStack.add(number);
            if (ch == '[') {

                charStack.add("");
                start++;
            } else if (ch == ']') {
                start++;
            } else {
                StringBuilder charSB = new StringBuilder();
                while (isAlphabeta(ch)) {
                    charSB.append(ch);
                    start++;
                    if (start >= chars.length) {
                        break;
                    }
                    ch = chars[start];
                }
                charStack.add(charSB.toString());
            }
        }
        System.out.println(numberStack);
        System.out.println(charStack);
        return result.toString();
    }

    private boolean isAlphabeta(char ch) {
        return ch >= 'A' && ch <= 'z' && ch != '[' && ch != ']';
    }

    private boolean isNumber(char ch) {
        return ch >= '0' && ch <= '9';
    }
}
