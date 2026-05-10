'''
store a set with the elements of nums
the set will have only unique elements
1. take each element from uniq and look for uniq[i] + 1 in uniq
2. if found, increment length
3. if not found, compare with max length
4. return max length
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        uniq = set(nums)
        max_lth = 1

        for i, num in enumerate(uniq):
            j = 1
            lth = 1

            while num + j in uniq:
                lth += 1
                j += 1
            
            max_lth = max(max_lth, lth)

        return max_lth
        