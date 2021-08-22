class Solution {
    public int trap(int[] arr) {
        if (arr == null || arr.length <= 2) {
            return 0;
        }
        int left = 0, right = arr.length - 1;
        int mark = Math.min(arr[left], arr[right]);
        int water = 0;
        while (left < right) {
            if (arr[left] < arr[right]) {
                left++;
                if (arr[left] < mark) {
                    water += mark - arr[left];
                } else {
                    mark = Math.min(arr[left], arr[right]);
                }
            } else {
                right--;
                if (arr[right] < mark) {
                    water += mark - arr[right];
                } else {
                    mark = Math.min(arr[left], arr[right]);
                }
            }
        }
        return water;
    }
}

class Solution {
    public int trap(int[] arr) {
        if (arr == null || arr.length <= 2) {
            return 0;
        }
        int max = arr[0];
        int[] leftWater = new int[arr.length];
        leftWater[0] = 0;
        for (int i = 1; i < arr.length; i++) {
            leftWater[i] = arr[i] < max ? max - arr[i] : 0;
            max = Math.max(max, arr[i]);
        }
            
        int[] rightWater = new int[arr.length];
        rightWater[arr.length - 1] = 0;
        max = arr[arr.length - 1];
        for (int i = arr.length - 2; i >= 0; i--) {
            rightWater[i] = arr[i] < max ? max - arr[i] : 0;
            max = Math.max(max, arr[i]);
        }
        int sum = 0;
        for (int i = 0; i < leftWater.length; i++) {
            sum += Math.min(leftWater[i], rightWater[i]);
        }
        return sum;
    }
}

class Solution {
    public int trap(int[] height) {
        Stack<Integer> stack = new Stack<>();
        int ans = 0;
        for (int i = 0; i < height.length; i++) {
            while (!stack.isEmpty() && height[i] > height[stack.peek()]) {
                int top = stack.pop();
                if (stack.isEmpty()) {
                    break;
                }
                int left = stack.peek();
                int curWidth = i - left - 1;
                int curHeight = Math.min(height[i], height[left]) - height[top];
                ans += curWidth * curHeight;
            }
            stack.push(i);
        }
        return ans;
    }
}