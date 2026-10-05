class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        low, high = 0, len(nums) - 1
        res = float("inf")

        while low <= high:
            mid = (low + high) // 2
            res = min(res, nums[mid])

            if nums[0] <= nums[mid]:
                low = mid + 1
            
            else:
                high = mid - 1


        return res