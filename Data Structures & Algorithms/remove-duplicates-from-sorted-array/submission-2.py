class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        k wil increment only if the number is unique
        if the number is unique increment k and insert at k\
        position of the array that unique number
        '''

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
