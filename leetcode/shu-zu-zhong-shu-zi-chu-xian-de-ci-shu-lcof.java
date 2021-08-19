class Solution {
    public int[] singleNumbers(int[] nums) {
        int res = 0;
        for (int num : nums) {
            res ^= num;
        }
        int split = 1;
        while ((split & res) == 0) {
            split <<= 1;
        }
        int a = 0, b = 0;
        for (int num : nums) {
            if ((split & num) == 0) {
                a ^= num;
            } else {
                b ^= num;
            }
        }
        return new int[]{a, b};
    }
}