class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] result = new int[m];
        for (int i = 0; i < m; i++) {
            result[i] = nums1[i];
        }
        int i = 0, j = 0, k = 0;
        while (i < m && j < n) {
            if (result[i] < nums2[j]) {
                nums1[k] = result[i];
                i++;
            } else {
                nums1[k] = nums2[j];
                j++;
            }
            k++;
        }
        while(i < m) {
            nums1[k] = result[i];
            i++;
            k++;
        }
        while(j < n) {
            nums1[k] = nums2[j];
            j++;
            k++;
        }
    }
}

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1, j = n - 1, k = m + n - 1;
        while (i >= 0 && j >= 0) {
            if (nums1[i] < nums2[j]) {
                nums1[k--] = nums2[j--];
            } else {
                nums1[k--] = nums1[i--];
            }
        }
        while(j >= 0) {
            nums1[k--] = nums2[j--];
        }
    }
}