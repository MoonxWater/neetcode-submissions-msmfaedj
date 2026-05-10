'''
create a set from nums
iterate over the set
1. check if cur el - 1 in set
2. if true, set length = 0 and increment while cur el + length in set
3. compare with max len
4. return max len
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        uniq = set(nums)
        max_len = 1

        for num in uniq:
            if num - 1 not in uniq:
                length = 0

                while num + length in uniq:
                    length += 1
                
                max_len = max(max_len, length)
        
        return max_len