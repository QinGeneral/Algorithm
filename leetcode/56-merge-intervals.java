package leetcode;

import java.util.ArrayList;
import java.util.Arrays;

class Solution56 {
    public static void main(String[] args) {
        System.out.println(
                Arrays.deepToString(new Solution56().merge(new int[][] { { 1, 3 }, { 2, 6 }, { 8, 10 }, { 15, 18 } })));
        System.out.println(Arrays.deepToString(new Solution56().merge(new int[][] { { 1, 4 }, { 4, 5 } })));
    }

    public int[][] merge(int[][] intervals) {
        ArrayList<int[]> result = new ArrayList<>();
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        int[] current = intervals[0];
        for (int i = 1; i < intervals.length; i++) {
            if (current[1] < intervals[i][0]) {
                result.add(current);
                current = intervals[i];
            } else {
                current[1] = Math.max(current[1], intervals[i][1]);
            }
        }
        result.add(current);

        int[][] resultArray = new int[result.size()][2];
        for (int i = 0; i < result.size(); i++) {
            resultArray[i] = result.get(i);
        }
        return resultArray;
    }
}