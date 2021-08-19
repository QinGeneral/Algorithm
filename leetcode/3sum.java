import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            List<Integer> temp = twoSum(nums, nums[i], i);
            res.add(temp);
        }
        return res;
    }

    public List<Integer> twoSum (int[] numbers, int target, int skipIndex) {
        HashMap<Integer, Integer> map = new HashMap<>();
        List<Integer> res = new ArrayList<>();

        for (int i = 0; i < numbers.length; i++) {
            if (i == skipIndex) {
                continue;
            }
            int temp = target - numbers[i];
            if (map.containsKey(numbers[i])) {
                res.add(target);
                res.add(numbers[i]);
                res.add(numbers[skipIndex]);
                Collections.sort(res);
                return res;
            } else {
                map.put(temp, i);
            }
        }
        return null;
    }
}