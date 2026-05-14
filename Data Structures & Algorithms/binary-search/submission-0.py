'''
two vars low and high
run loop until low <= high
calc mid = (low + high) // 2
check if el at mid is target, and return if true
if el is greater than target, move high to mid - 1
else move low to mid + 1
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1