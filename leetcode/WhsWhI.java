class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        Arrays.sort(nums);
        int maxLength = 1;
        int curLength = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] - nums[i - 1] == 1) {
                curLength++;
            } else if ( nums[i] == nums[i -1]) {
                // do nothing
            } else {
                maxLength = Math.max(maxLength, curLength);
                curLength = 1;
            }
        }
        maxLength = Math.max(maxLength, curLength);
        return maxLength;
    }
}

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        Set<Integer> set = new HashSet<Integer>();
        for (int num : nums) {
            set.add(num);
        }
        int maxLength = 0;
        for (int num : nums) {
            if (!set.contains(num - 1)) {
                int t = 1, next = num + 1;
                while (set.contains(next++)) {
                    t++;
                }
                maxLength = Math.max(maxLength, t);
            }
        }
        return maxLength;
    }
}