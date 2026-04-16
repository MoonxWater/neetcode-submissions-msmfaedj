class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        O(n) space is simple but what about optimal?
  
        '''

        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)

        max_cnt = float('-inf')
        num = nums[0]

        for i in freq:
            if freq[i] > max_cnt:
                max_cnt = freq[i]
                num = i

        return num