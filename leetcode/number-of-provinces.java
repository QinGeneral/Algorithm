class Solution {

    int count = 0;
    public int findCircleNum(int[][] isConnected) {
        for (int i = 0; i < isConnected.length; i++) {
            sweap(isConnected, i, true);
        }
        return count;
    }
    
    public void sweap(int[][] isConnected, int i, boolean isCount) {
        if (i < 0 || i >= isConnected.length) {
            return;
        }
        if (isCount && isConnected[i][i] == 1) {
            count++;
        }
        if (!isCount) {
            isConnected[i][i] = 0;
        }
        for (int j = 0; j < isConnected.length; j++) {
            if (isConnected[i][j] == 1) {
                isConnected[i][j] = 0;
                isConnected[j][i] = 0;
                sweap(isConnected, j, false);
            }
        }
    }
}

class Solution {

    int count = 0;
    boolean[] isVisited;
    public int findCircleNum(int[][] isConnected) {
        isVisited = new boolean[isConnected.length];
        for (int i = 0; i < isConnected.length; i++) {
            if (!isVisited[i]) {
                count++;
                sweap(isConnected, i);
            }
        }
        return count;
    }
    
    public void sweap(int[][] isConnected, int i) {
        for (int j = 0; j < isConnected.length; j++) {
            if (!isVisited[j] && isConnected[i][j] == 1) {
                isVisited[j] = true;
                sweap(isConnected, j);
            }
        }
    }
}

class Solution {

    int count = 0;
    int[] unionArray;
    public int findCircleNum(int[][] isConnected) {
        unionArray = new int[isConnected.length];
        for (int i = 0; i < isConnected.length; i++) {
            unionArray[i] = i;
        }
        for (int i = 0; i < isConnected.length; i++) {
            for (int j = i + 1; j < isConnected.length; j++) {
                if (isConnected[i][j] == 1) {
                    union(i, j);
                }
            }
        }
        for (int i = 0; i < isConnected.length; i++) {
            if (unionArray[i] == i) {
                count++;
            }
        }
        return count;
    }
    
    public void union(int i, int j) {
        unionArray[find(i)] = find(j);
    }

    public int find(int i) {
        if (unionArray[i] != i) {
            unionArray[i] = find(unionArray[i]);
        }
        return unionArray[i];
    }
}