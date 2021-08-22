class Solution {
    int[] backup, temp;

    public int reversePairs(int[] nums) {
        backup = new int[nums.length];

        return getReversePairs(nums, 0, nums.length - 1);
    }

    public int getReversePairs(int[] nums, int left, int right) {
        if (left >= right) {
            return 0;
        }
        int mid = (left + right) / 2;
        int leftRP = getReversePairs(nums, left, mid);
        int rightRP = getReversePairs(nums, mid + 1, right);

        int curRP = mergeAndCount(nums, left, mid, right);
        return leftRP + rightRP + curRP;
    }

    private int mergeAndCount(int[] nums, int left, int mid, int right) {
        for (int i = left; i <= right; i++) {
            backup[i] = nums[i];
        }

        int i = left;
        int j = mid + 1;

        int count = 0;
        for (int k = left; k <= right; k++) {
            if (i == mid + 1) {
                nums[k] = backup[j];
                j++;
            } else if (j == right + 1) {
                nums[k] = backup[i];
                i++;
            } else if (backup[i] <= backup[j]) {
                nums[k] = backup[i];
                i++;
            } else {
                nums[k] = backup[j];
                j++;
                count += (mid - i + 1);
            }
        }
        return count;
    }
}