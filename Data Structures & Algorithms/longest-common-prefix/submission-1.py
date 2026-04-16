'''
a prefix array initialised to the first element of strs array

start with the second element and compare the prefix till a mismatch
is found or len of prefix or current element is exhausted.

if the len of prefix is exhausted, move on
else if the len of current element if exhausted, the current element
becomes prefix



return prefix
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = [char for char in strs[0]]

        for i in range(len(strs)):
            if strs[i] == '': return ''
            
            j = 0

            while j < len(strs[i]) and j < len(prefix):
                if strs[i][j] != prefix[j]:
                    prefix = prefix[:j]
                    break
                j += 1

            else:
                prefix = prefix[:min(len(strs[i]), len(prefix))]

        
        return ''.join(prefix)


