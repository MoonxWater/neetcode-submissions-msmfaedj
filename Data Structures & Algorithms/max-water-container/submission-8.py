class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        two pointers at both ends
        move the pointer inward that has smaller value of height
        this is because the one with greater height does not
        contribute anything to the capacity via its height
        and moving that side will only decrease the width thereby
        decreasing the capacity

        one capacity variable to store capacity

        at each move inwards at either sides, calculate the capacity 
        with that pointer and update capacity if it is more than 
        what we currently have

        return capacity
        '''
        l = 0
        r = len(heights) - 1
        max_capacity = 0

        while l < r:
            cur_capacity = min(heights[l], heights[r]) * (r - l)
            max_capacity = max(cur_capacity, max_capacity)
            
            if heights[l] <= heights[r]:
                l += 1

            else:
                r -= 1
                
        return max_capacity