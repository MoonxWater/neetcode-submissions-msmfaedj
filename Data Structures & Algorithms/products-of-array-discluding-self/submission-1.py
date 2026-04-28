'''
keep a running product and append to rightward_prod
rightward_prod[i] will be equal to the product of all the previous
elements except self.

reiterate from backwards and do the same thing
with leftward_prod
same with leftward[i]

combine them by multiplying and append to output
Note: leftward_prod is appending in reversed order
ie, the first element is the last from nums
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        rightward_prod = []
        leftward_prod = []
        right_prod = 1
        left_prod = 1

        for i in range(len(nums)):
            rightward_prod.append(right_prod)
            right_prod *= nums[i]

            leftward_prod.append(left_prod)
            left_prod *= nums[len(nums) - i - 1]

        for j in range(len(nums)):
            if j < 1:
                output.append(leftward_prod[-1])

            elif j == len(nums) - 1:
                output.append(rightward_prod[-1])

            else:
                output.append(rightward_prod[j] * leftward_prod[len(nums) - j -1])

        return output