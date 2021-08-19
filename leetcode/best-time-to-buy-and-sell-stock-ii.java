class Solution {
    public int maxProfit(int[] prices) {
        int[] dp = new int[prices.length];
        dp[0] = 0;
        for (int i = 1; i < prices.length; i++) {
            int profit = prices[i] - prices[i - 1];
            dp[i] = dp[i - 1] + (profit > 0 ? profit : 0);
        }
        return dp[prices.length - 1];
    }
}