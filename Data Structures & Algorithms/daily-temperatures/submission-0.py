"""
set a result arr and put 0 len times
iterate over the temp arr
while cur temp is greater than top of rem temp, pop from rem temp and update 
    result arr with the diff of (cur temp and top temp)idx
add cur temp to rem stack

return result
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        rem_temp = []

        for i, temp in enumerate(temperatures):
            while rem_temp and temp > rem_temp[-1][1]:
                top_idx, top_temp = rem_temp.pop()
                result[top_idx] = i - top_idx
            
            rem_temp.append((i, temp))

        return result




        