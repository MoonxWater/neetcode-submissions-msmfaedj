class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        freq = []
        result = []
        taken = []

        for i in range(len(strs)):
            freq.append({})
            for char in strs[i]:
                freq[i][char] = 1 + freq[i].get(char, 0)

        for i in range(len(strs)):
            if strs[i] in taken:
                continue
            result.append([strs[i]])
            
            for j in range(i + 1, len(strs)):
                if freq[i] == freq[j]:
                    result[-1] += [strs[j]]
                    taken.append(strs[j])
                if strs[i] not in taken: taken.append(strs[i])
            
        return result
