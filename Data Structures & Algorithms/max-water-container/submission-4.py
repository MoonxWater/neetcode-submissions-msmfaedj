class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_water = min(heights[l], heights[r]) * (r - l)
        
        while l < r:
            if heights[l] <= heights[r]:
                l += 1
            
            else:
                r -= 1
            

            cur_water = min(heights[l], heights[r]) * (r - l)

            if cur_water > max_water:
                max_water = cur_water


        return max_water