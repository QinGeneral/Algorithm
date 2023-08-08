package leetcode;

class Solution11 {
    public static void main(String[] args) {
        int[] heights = new int[] { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
        System.out.println(new Solution11().maxArea(heights));
    }

    public int maxArea(int[] height) {
        int max = 0;

        int start = 0;
        int end = height.length - 1;
        while (start < end) {
            int cur = (end - start) * Math.min(height[start], height[end]);
            max = Math.max(max, cur);
            if (height[start] < height[end]) {
                start++;
            } else {
                end--;
            }
        }
        return max;
    }
}
