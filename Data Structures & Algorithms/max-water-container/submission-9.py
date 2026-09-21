class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0

        while l < r:
            width = r - l
            if heights[l] <= heights[r]:
                max_water = max(max_water, width * heights[l])
                l += 1

            else:
                max_water = max(max_water, width * heights[r])
                r -= 1

        return max_water
