'''
the brute force solution
2 loops: 0 to n - 1 and the other 0 to n - 1 with i being skipped
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            output.append(1)

            for j in range(len(nums)):
                if i == j:
                    continue

                output[i] *= nums[j]     

        return output