'''
hash all elements with their freqs
sort freqs.items() according to freq
create a ret var with the last k elements
return ret
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        
        for num in nums:
            freqs[num] = 1 + freqs.get(num, 0)

        freqs = sorted(freqs.items(), key=lambda x: x[1])
        ret = [num_pair[0] for i, num_pair in enumerate(freqs) if i + k >= len(freqs)]
        
        return ret

        