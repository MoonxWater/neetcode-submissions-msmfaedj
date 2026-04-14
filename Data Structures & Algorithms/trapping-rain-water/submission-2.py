class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        one pointer at start
        update pointer till l + 1 is smaller than l 
        after that a new pointer will go till r + 1 is smaller then r
            (this implies that the water will fall beyond this point)
        update capacity at every increment of r with height[l] - height[r]

        calc min(height[l], height[r])
        if height[l] is smaller move on
        else subtract from capacity (height[l] - height[r]) * (r - l)

        update l to be r and repeat the process
        
        there is a variable to store capacity
        

        remember to subtract width from all the calculations
        
        max water to trap = min(height[l], height[r]) * (r - l - 1) 
                            - (all heights between l and r)

        '''
        if len(height) <= 2: return 0

        l = 0
        capacity = 0
        r = 1
        boundary = len(height) - 1

        while height[l] <= height[l + 1]:
            l += 1
        
        while height[boundary] <= height[boundary - 1]:
            boundary -= 1

        while l < boundary and r < boundary:        
            r = l + 1
            rocks_list = []
            rocks = 0

            while r < boundary and height[r] < height[l]:
                rocks_list.append(height[r])
                r += 1
            
            min_height = min(height[l], height[r])

            for i, rock in enumerate(rocks_list):
                if rock >= min_height:
                    rocks += min_height
                else:
                    rocks += rock

            capacity += (min_height * (r - l - 1)) - rocks
            l = r
        
        return capacity