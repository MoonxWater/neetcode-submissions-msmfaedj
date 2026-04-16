class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        how about we sort it first
        then keep two counter variables. one for the max
        count and one for the current number
        if counter for the current number is more than the 
        counter for the max count, update max count
        '''

        nums.sort()
        
        num = nums[0]
        max_cnt = 1
        cur_cnt = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if cur_cnt > max_cnt:
                    max_cnt = cur_cnt
                    num = nums[i - 1]

                cur_cnt = 0

            cur_cnt += 1

        if cur_cnt > max_cnt:
            num = nums[-1]
        
        return num 