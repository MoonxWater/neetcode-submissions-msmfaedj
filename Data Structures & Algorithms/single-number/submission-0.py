'''
#using xor approach
    since every number appears twice, each pair would
    ouput 0 when xored except for that one number which
    appears once. hence the xor of every element will be
    that number.
#initialise a "xor" variable with 0
#loop throught the input array and xor each number with
the "xor" variable
#return "xor"
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0

        for num in nums:
            xor ^= num

        return xor