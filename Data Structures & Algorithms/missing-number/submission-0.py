class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        let's do this the binary search way
        '''
        nums.sort()

        if nums[0] != 0:
            return 0

        low = 0
        high = len(nums)
        mid = (high + low) // 2

        while low < high:
            mid = (low + high) // 2

            if nums[mid] == mid:
                low = mid + 1
            
            elif nums[mid] == mid + 1:
                if nums[mid - 1] == mid - 1:
                    return mid

                else:
                    high = mid

        return len(nums) 
            
