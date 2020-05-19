package sort;

import java.util.Arrays;

public class insert_sort {
    public static void main(String[] args) {
        Arrays.sort(new int[8]);

        int[] a = { 1, 3, 6, 5, 1, 2, -1 };
        insertionSort(a, 0, a.length);
        for (int item : a) {
            System.out.print(item);
        }
    }

    // 插入排序，此代码来自 Arrays.sort 中的插入排序
    private static void insertionSort(int[] a, int low, int high) {
        for (int i, k = low; ++k < high;) {
            int ai = a[i = k];

            if (ai < a[i - 1]) {
                while (--i >= low && ai < a[i]) {
                    a[i + 1] = a[i];
                }
                a[i + 1] = ai;
            }
        }
    }
}