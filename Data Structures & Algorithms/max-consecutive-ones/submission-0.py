class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt = cur_cnt = 0

        for bit in nums:
            if not bit:
                max_cnt = max(max_cnt, cur_cnt)
                cur_cnt = 0
            else:
                cur_cnt += 1

        return max(max_cnt, cur_cnt)