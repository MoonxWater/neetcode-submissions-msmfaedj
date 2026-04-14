'''
i don't know how to encode a string but i can try
i have done something similar before.

i got a great idea. how about i convert all 
characters to their ascii number and join them using a delimiter
there is no way that if the delimiter is within the strs array,
it would make it to the s string because it would be converted.
i would also need a letter delimiter
'''

class Solution:
    delimiter = '%'
    ltr_delimiter = '/'

    def encode(self, strs: List[str]) -> str:
        if strs == []: return '' 
        encoded = []

        for i in range(len(strs)):
            if len(strs[i]) == 0:
                encoded.append(self.delimiter)
                continue

            for j in range(len(strs[i])):
                encoded.append(str(ord(strs[i][j])))
                encoded.append(self.ltr_delimiter)

            encoded.append(self.delimiter)

        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        if s == '': return []

        strs = [[]]
        word = 0
        temp = []

        for i in range(len(s)):
            if s[i] == self.delimiter:
                word += 1
                strs.append([])

            elif s[i] == self.ltr_delimiter:
                strs[word] += chr(int(''.join(temp)))
                temp.clear()

            else:
                temp.append(s[i])
        
        return [''.join(item) for i, item in enumerate(strs) if i < len(strs) - 1]


        