class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        mistake: res += word[i] takes O(n) time as it creates a brand 
        new string and copies all the elements thus making my prev
        sol O(n^2) as compared to the optimal O(n).

        to solve this problem, instead of res as a string, make it a list
        and append the char at the end of the list which would take 
        O(1)

        before return use ''.join(res) to do this in O(n).
        '''

        i = j = 0
        res = []

        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])

            i += 1
            j += 1
            
            
        res.extend(word1[i:])
        res.extend(word2[j:])

        return ''.join(res)