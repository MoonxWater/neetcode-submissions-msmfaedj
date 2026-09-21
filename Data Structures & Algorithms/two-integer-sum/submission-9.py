class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needs = {}

        for i, num in enumerate(nums):
            needed = target - num
            
            if needed in needs:
                return [needs[needed], i]
            
            needs.update({num: i})

        return []