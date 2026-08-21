class Solution {
    public int[] twoSum(int[] nums, int target) {
        /*
        loop through the array and store the needed val by each element
        loop through the array again and this time, try to find that val.
        */

        Map<Integer, Integer> needs = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int needed = target - nums[i];

            if (needs.containsKey(nums[i]) && needs.get(nums[i]) != i) {
                return new int[] {needs.get(nums[i]), i};
            }

            needs.put(needed, i);
        }
        System.out.println(needs);
        return new int[] {};
    }
}
