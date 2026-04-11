class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)): return False

        seen = []

        for num in nums:
            if num in seen: return True

            seen.append(num)

        return False