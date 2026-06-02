'''
keep an array with running prod of the elements

keep another array with the running prod of elements
but from the opp dir

mul both the elements at that idx and append to output
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = []
        right_prod = []
        output = []
        prod = 1

        for num in nums:
            left_prod.append(prod)
            prod *= num

        prod = 1

        for num in reversed(nums): 
            right_prod.append(prod) 
            prod *= num

        for i in range(len(nums)):
            output.append(left_prod[i] * right_prod[len(nums) - i - 1])

        return output