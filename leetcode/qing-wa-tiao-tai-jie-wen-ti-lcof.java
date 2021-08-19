class Solution {
    HashMap<Integer, Integer> map = new HashMap<>();
    public int numWays(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        if (map.containsKey(n)) {
            return map.get(n);
        }
        int r = numWays(n - 1) + numWays(n - 2);
        r = r % 1000000007;
        map.put(n, r);
        return r;
    }
}