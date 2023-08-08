package leetcode;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Stack;

class Solution20 {
    public static void main(String[] args) {
        System.out.println(new Solution20().isValid("{[]}"));
    }

    public boolean isValid(String s) {
        LinkedList<Character> stack = new LinkedList<>();

        Map<Character, Character> map = new HashMap<>();
        map.put('}', '{');
        map.put(']', '[');
        map.put(')', '(');
        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.add(ch);
            } else {
                if (stack.peekLast() == map.get(ch)) {
                    stack.pollLast();
                } else {
                    stack.add(ch);
                }
            }
        }
        if (stack.size() > 0) {
            return false;
        }
        return true;
    }
}