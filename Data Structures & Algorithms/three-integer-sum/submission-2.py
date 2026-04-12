class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        variables needed:
            1. maybe cur_sum = nums[l] + nums[r]?
            2. res variable which would be a set with O(1) lookup
                and unique value but list is not hashable so convert 
                to tuple
            3. pointer l with start at index i and moves right at if true
            4. pointer r with start at n - 1 and moves left at elif true
            5. target which will store -nums[i] so that we compare
                cur_sum with target and decide which pointer to move
        '''
        res = set()
        nums.sort()
        '''
        there are two loop, one outer and one inner
        '''

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]

            '''
            at every iteration, i will make a target which would 
            be equal to 0 - that number bcz
                a + b + c = 0
                thrfore b + c = 0 - a(that number chosen through outer loop)
                that -a would then become the target that needs to be 
                reached with the rest of the elements
            this will reduce the problem into two parts
            1. the outer loop which selects the target
            2. the inner loop which is simply 2 sum problem
            '''

            while l < r:
                cur_sum = nums[l] + nums[r]

                if cur_sum < target:
                    l += 1
                elif cur_sum > target:
                    r -=1

                    '''
                    if the rest of the elements are able to reach -a, add 
                    that triplet to the result if not already in result
                    and move on to the next iteration

                    the addtion should be made with sorted triplets so the 
                    comparison is simpler
                    '''
                else:
                    '''
                    something unique about this, after adding to res
                    increment l and decrement r
                    since we do both at the same time, there is a chance
                    that the sum remains intact and we get another triplet

                    '''
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                    r -= 1
                         
                
        '''
        return res as a list
        '''
        return list(res)