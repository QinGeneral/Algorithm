class Solution {
    public int nthUglyNumber(int n) {
        int[] factores = new int[]{2, 3, 5};
        Set<Long> seen = new HashSet<Long>();
        PriorityQueue<Long> queue = new PriorityQueue<>();

        queue.add(1L);
        int count = 0;
        long ungly = 1L;
        while (count < n) {
            ungly = queue.poll();
            for (int i = 0; i < factores.length; i++) {
                long num = ungly * factores[i];
                if (!seen.contains(num)) {
                    queue.offer(num);
                    seen.add(num);
                }
            }
            count++;
        }

        return (int) ungly;
    }
}

class Solution {
    public int nthUglyNumber(int n) {
        int[] factores = new int[]{2, 3, 5};

        int[] dp= new int[n];
        dp[0] = 1;
        int p2 = 0;
        int p3 = 0;
        int p5 = 0;

        for (int i = 1; i < n; i++) {
            long n2 = dp[p2] * 2, n3 = dp[p3] * 3, n5 = dp[p5] * 5;
            dp[i] = (int) Math.min(n2, Math.min(n3, n5));
            if (dp[i] == n2) {
                p2++;
            }
            if (dp[i] == n3) {
                p3++;
            } 
            if (dp[i] == n5){
                p5++;
            }
        }
        return dp[n - 1];
    }
}