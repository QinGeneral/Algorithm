class Solution {
    public String convert(String s, int numRows) {

        if (numRows == 1) return s;

        List<StringBuilder> rows = new ArrayList<>();
        for (int i = 0; i < Math.min(numRows, s.length()); i++)
            rows.add(new StringBuilder());

        int curRow = 0;
        boolean goingDown = false;

        for (char c : s.toCharArray()) {
            rows.get(curRow).append(c);
            if (curRow == 0 || curRow == numRows - 1) goingDown = !goingDown;
            curRow += goingDown ? 1 : -1;
        }

        StringBuilder ret = new StringBuilder();
        for (StringBuilder row : rows) ret.append(row);
        return ret.toString();
    }
}

class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        String[] result = new String[numRows];
        int i = 0;
        int row = 0;
        boolean isDown = true;
        while (i < s.length()) {
            if (result[row] == null) {
                result[row] = s.substring(i, i + 1);
            } else {
                result[row] += s.substring(i, i + 1);
            }
            i++;
            if (isDown) {
                if (row == numRows - 1) {
                    row--;
                    isDown = false;
                } else {
                    row++;
                }
            } else {
                if (row == 0) {
                    row++;
                    isDown = true;
                } else {
                    row--;
                }
            }
        }
        String r = "";
        for (i = 0; i < result.length; i++) {
            if (result[i] == null)
                continue;
            r += result[i];
        }
        return r;
    }

    public static void main(String[] args) {
        System.out.println(new Solution().convert("PAYPALISHIRING", 3));
    }
}