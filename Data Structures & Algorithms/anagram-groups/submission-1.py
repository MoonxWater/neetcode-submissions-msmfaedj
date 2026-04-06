class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        result = []
        taken = []

        for i in range(len(strs)):
            if strs[i] in taken:
                continue
            result.append([strs[i]])
            
            for j in range(i + 1, len(strs)):
                if len(strs[i]) == len(strs[j]) and self.isAnagram([strs[i]], [strs[j]]):
                    result[-1] += [strs[j]]
                    taken.append(strs[j])
                if strs[i] not in taken: taken.append(strs[i])
            
            
        
        return result
            
        
    def isAnagram(self, s: list, t: list) -> bool:
        if len(s[0]) != len(t[0]): return False
        
        freq1 = {}
        freq2 = {}

        for i in range(len(s[0])):
            freq1[s[0][i]] = 1 + freq1.get(s[0][i], 0)
            freq2[t[0][i]] = 1 + freq2.get(t[0][i], 0)

        return freq1 == freq2