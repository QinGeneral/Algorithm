package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

class Solution {

  public static void main(String[] args) {
    int[] data = new int[] { -1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4 };
    System.out.println(Arrays.toString(data));
    System.out.println(new Solution().threeSum(data));

    System.out.println(new Solution().threeSumPointer(data));
  }

  List<List<Integer>> res = new ArrayList<>();

  public List<List<Integer>> threeSumPointer(int[] nums) {
    Arrays.sort(nums);
    for (int i = 0; i < nums.length; i++) {
      if (i > 0 && nums[i] == nums[i - 1]) {
        continue;
      }
      int start = i + 1;
      int end = nums.length - 1;
      while (start < end) {
        int sum = nums[i] + nums[start] + nums[end];
        if (sum == 0) {
          List<Integer> tmp = new ArrayList<>();
          tmp.add(nums[i]);
          tmp.add(nums[start]);
          tmp.add(nums[end]);
          res.add(tmp);
          start++;
          end--;
          while (start < end && nums[start] == nums[start - 1]) {
            start++;
          }
          while (start < end && nums[end] == nums[end + 1]) {
            end--;
          }
        } else if (sum < 0) {
          start++;
        } else {
          end--;
        }
      }
    }
    return res;
  }

  public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    for (int i = 0; i < nums.length; i++) {
      if (i > 0 && nums[i] == nums[i - 1]) {
        continue;
      }
      twoSum(nums, -nums[i], i);
    }
    return res;
  }

  public void twoSum(int[] numbers, int target, int skipIndex) {
    HashMap<Integer, Integer> map = new HashMap<>();

    for (int i = 0; i < numbers.length; i++) {
      if (i == skipIndex) {
        continue;
      }
      int temp = target - numbers[i];
      if (map.containsKey(numbers[i])) {
        List<Integer> tmp = new ArrayList<>();
        tmp.add(numbers[i]);
        tmp.add(numbers[map.get(numbers[i])]);
        tmp.add(-target);
        Collections.sort(tmp);
        if (!res.contains(tmp)) {
          res.add(tmp);
        }
      } else {
        map.put(temp, i);
      }
    }
  }

  public List<Integer> twoSumSlow(int[] numbers, int target, int skipIndex) {
    List<Integer> res = new ArrayList<>();

    for (int i = 0; i < numbers.length; i++) {
      if (i == skipIndex) {
        continue;
      }
      for (int j = 0; j < numbers.length; j++) {
        if (j == skipIndex) {
          continue;
        }
        if (numbers[i] + numbers[j] == target) {
          res.add(numbers[i]);
          res.add(numbers[j]);
          return res;
        }
      }
    }
    return res;
  }
}
