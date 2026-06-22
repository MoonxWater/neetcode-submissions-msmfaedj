'''
whenever we get the mid to land, one part of the array
will always be sorted whether that be the left or the 
right

assign low and high to 0 and len - 1
run a loop till low <= high
calc mid of low and high

if el at mid is equal to target, return mid
check if the el at mid is greater than the first el
if true, left half is sorted
check if target is within left half
if true, eliminate the right half
if false, eliminate the left half
if mid is smaller than first el, right half is sorted
check if target is in right half
if true, eliminate the left half
if false, eliminate the right half
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] >= nums[0]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1 
            
