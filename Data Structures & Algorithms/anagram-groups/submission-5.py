'''
sort the word and append to a freq dict with the sorted 
word as the key and a list as the value.

return a list of the values list
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for i, word in enumerate(strs):
            sorted_word = ''.join(sorted(word))
            if sorted_word in freq:
                freq[sorted_word].append(word)

            else:
                freq[sorted_word] = [word]            

        return list(freq.values())