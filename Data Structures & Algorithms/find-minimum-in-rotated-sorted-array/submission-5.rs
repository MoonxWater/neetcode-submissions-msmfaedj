impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        if nums[0] < nums[nums.len() - 1] {
            return nums[0] as i32
        }

        let mut low = 0;
        let mut high = nums.len() - 1;

        while low < high {
            let mut mid = (high + low) / 2;

            if nums[high] > nums[mid] {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        nums[low] as i32

    }
}
