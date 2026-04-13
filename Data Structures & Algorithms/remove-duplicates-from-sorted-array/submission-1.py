class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        one variable k:
        k will increment every time the element is unique
        k will not increment if the element is equal to the prev element
        k will start at 1

        '''

        k = 1

        while k < len(nums):
            if nums[k] == nums[k - 1]:
                nums.pop(k)
                continue     
            k += 1
            
        return k