class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        xor approach
        xor = len of nums
        loop over the array
        xor i with xor
        xor arr[i] with xor
        '''

        xor = len(nums)

        for i in range(len(nums)):
            xor ^= i ^ nums[i]

        return xor