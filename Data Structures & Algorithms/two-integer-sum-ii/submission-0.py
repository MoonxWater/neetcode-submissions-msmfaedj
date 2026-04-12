class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        the loop should go till the element is smaller than the target
        if the element is equal to or greater than the target, it is
        not a possible solution anymore

        let us make an index i and 
        another index j will be kept at the end

        since there is one possible solution in every set,
        we will add the elements at i and j
        if the sum is less than target, increment i
        if the sum is greater than target, decrement j


        '''
        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            
            elif numbers[i] + numbers[j] > target:
                j -= 1

            else:
                return [i + 1, j + 1]