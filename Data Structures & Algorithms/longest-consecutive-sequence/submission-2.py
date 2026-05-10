'''
store all elements in a set
2 vars to store length -> max len and len
1. loop over the set and look for next number in the set
2. increment length
3. remove every next element found from the set
4. after not finding any more elements, look for the prev 
    elements and increment len if found, remove them
5. remove the element
6. compare len with max len
7. return max len 
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        uniq = set(nums)
        max_len = 1
        
        for num in nums:
            if num not in uniq:
                continue

            j = 1
            lth = 1

            while num + j in uniq:
                lth += 1
                uniq.remove(num + j)
                j += 1
            
            j = 1
            
            while num - j in uniq:
                lth += 1
                uniq.remove(num - j)
                j += 1
            
            uniq.remove(num)

            max_len = max(max_len, lth)

        return max_len
        