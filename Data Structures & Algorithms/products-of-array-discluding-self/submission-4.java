class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] output = new int[n];
        int prod = 1;

        for (int i = 0; i < n; i++) {
            output[i] = prod;    
            prod *= nums[i];
        }
        
        prod = 1;

        for (int j = n - 1; j >= 0; j--) {
            output[j] *= prod;
            prod *= nums[j];
        }

        return output;
    }
}  
