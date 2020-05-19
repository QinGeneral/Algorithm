import java.util.Arrays;

public class test {
    public static void main(String[] args) {
        System.out.print(0 & 1);
        Arrays.sort(new int[8]);

        int[] a = {1, 3, 6, 5, 1, 2, -1};
        insertionSort(a, 0, a.length);
        for (int item: a) {
            System.out.print(item);
        }
    }

    private static void insertionSort(int[] a, int low, int high) {
        for (int i, k = low; ++k < high; ) {
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