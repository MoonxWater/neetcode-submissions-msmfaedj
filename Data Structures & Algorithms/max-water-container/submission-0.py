class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        total water in container = min height of two * diff in index
        '''

        max_water = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                if min(heights[i], heights[j]) * (j - i) > max_water:
                    max_water = min(heights[i], heights[j]) * (j - i)

        return max_water