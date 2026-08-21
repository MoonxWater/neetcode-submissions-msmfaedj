class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> needs = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int needed = target - nums[i];

            if (needs.containsKey(nums[i])) {
                return new int[] {needs.get(nums[i]), i};
            }

            needs.put(needed, i);
        }

        return new int[] {};
    }
}
