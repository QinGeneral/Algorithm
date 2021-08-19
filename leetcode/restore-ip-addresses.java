class Solution22 {
    public int mySqrt(int x) {
        if (x == 0) {
            return 0;
        }
        int l = 1, r = x;
        while (l < r - 1) {
            int mid = l + (r - l) / 2;
            if (mid * mid == x) {
                return mid;
            } else if (mid * mid > x) {
                r = mid;
            } else {
                l = mid;
            }
        }
        return l;
    }

    public static void main(String[] args) {
        System.out.println(new Solution22().mySqrt(2147395599));
    }
}