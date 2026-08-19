
import java.util.HashSet;
import java.util.Set;

class Solution {

    public boolean containsDuplicate(int[] nums) {

        Set<Integer> seen = new HashSet<>();

        for (int num : nums) {

            if (seen.contains(num)) {
                return true;
            }

            seen.add(num);
        }

        return false;
    }

    public static void main(String[] args) {

        int[] nums = { 1, 2, 3, 1 };

        Solution solution = new Solution();

        boolean result = solution.containsDuplicate(nums);

        System.out.print("Input: [");

        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i]);

            if (i < nums.length - 1) {
                System.out.print(", ");
            }
        }

        System.out.println("]");

        System.out.println("Output: " + result);
    }
}