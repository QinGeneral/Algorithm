class Solution {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) {
            return "0";
        }
        StringBuilder res = new StringBuilder("0");
        int add = 0;
        int i = num2.length() - 1;
        while (i >= 0) {
            StringBuilder temp = multi(num1, num2.charAt(i) - '0');
            for (int j = 0; j < (num2.length() - 1 - i); j++) {
                temp.append("0");
            }
            i--;
            res = add(temp, res);
        }
        return res.toString();
    }

    public StringBuilder add(StringBuilder num1, StringBuilder num2) {
        int add = 0;
        int i = num1.length() - 1;
        int j = num2.length() - 1;
        StringBuilder res = new StringBuilder();
        while (i >= 0 || j >= 0) {
            int a = i >= 0 ? (num1.charAt(i--) - '0') : 0;
            int b = j >= 0 ? (num2.charAt(j--) - '0') : 0;
            int r = a + b + add;
            add = r / 10;
            res.insert(0, r % 10);
        }
        if (add > 0) {
            res.insert(0, add);
        }
        return res;
    }

    public StringBuilder multi(String num, int num2) {
        int i = num.length() - 1;
        StringBuilder res = new StringBuilder();
        int add = 0;
        while (i >= 0) {
            int r = (num.charAt(i--) - '0') * num2 + add;
            add = r / 10;
            res.insert(0, r % 10);
        }
        if (add > 0) {
            res.insert(0, add);
        }
        return res;
    }
}