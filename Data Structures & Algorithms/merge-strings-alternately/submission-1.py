class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        res = ''
        switch = True

        while i < len(word1) and j < len(word2):
            if switch:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1
            
            switch = not(switch)
        
        res += word1[i:]
        res += word2[j:]

        return res