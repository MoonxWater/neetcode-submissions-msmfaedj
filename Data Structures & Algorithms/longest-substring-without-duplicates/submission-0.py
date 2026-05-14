'''
return 0 if input empty
longest var, cur_len
two pointers l r
loop over the string
check if char at r in window
if not in window, add to set and r++
if in window, remove the char at l and l++
everytime r++ check len
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        longest = 0
        l = r = 0

        while r < len(s):
            if s[r] not in s[l:r]:
                r += 1
                longest = max(longest, r - l)
            else:
                l += 1

        return longest
