class Solution {
    public int maximalSquare(char[][] matrix) {
        int max = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] == '1') {
                    max = Math.max(max, getMax(matrix, i, j));
                }
            }
        }
        return max * max;
    }

    public int getMax(char[][] matrix, int i, int j) {
        int max = 1;
        while (true) {
            boolean isSqure = true;
            for (int k = 0; k < max + 1; k++) {
                int rowI = i + max;
                int rowJ = j + k;
                if (rowI >= matrix.length || rowJ >= matrix[rowI].length || matrix[rowI][rowJ] == '0') {
                    isSqure = false;
                    break;
                }
                int columnI = i + k;
                int columnJ = j + max;
                if (columnI >= matrix.length || (columnJ) >= matrix[columnI].length || matrix[columnI][columnJ] == '0') {
                    isSqure = false;
                    break;
                }
            }
            if (!isSqure) {
                break;
            }
            max++;
        }
        return max;
    }
}

class Solution {
    public int maximalSquare(char[][] matrix) {
        int[][] dp = new int[matrix.length][matrix[0].length];

        int max = 0;
        for (int i = 0; i < matrix.length; i++) {
            dp[i][0] = matrix[i][0] == '1' ? 1 : 0;
            max = Math.max(dp[i][0], max);
        }
        for (int i = 0; i < matrix[0].length; i++) {
            dp[0][i] = matrix[0][i] == '1' ? 1 : 0;
            max = Math.max(dp[0][i], max);
        }

        for (int i = 1; i < matrix.length; i++) {
            for (int j = 1; j < matrix[i].length; j++) {
                if (matrix[i][j] == '0') {
                    dp[i][j] = 0;
                } else {
                    dp[i][j] = Math.min(Math.min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1;
                    max = Math.max(dp[i][j], max);
                }
            }
        }
        return max * max;
    }
}