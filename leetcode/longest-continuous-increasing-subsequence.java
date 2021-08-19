class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int max = 0;
        int cur = 1;
        int i= 0;
        while (i < nums.length -1 ) {
            if (nums[i] < nums[i + 1]) {
                cur++;
            } else {
                if (cur > max) {
                    max = cur;
                }
                cur = 1;
            }
            i++;
        }
        if (cur > max) {
            max = cur;
        }
        return max;
    }
}