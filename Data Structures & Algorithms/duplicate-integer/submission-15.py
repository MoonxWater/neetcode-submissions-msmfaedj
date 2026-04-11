class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)) or nums == []: return False

        seen = set()

        for num in nums:
            if num in seen: return True

            seen.add(num)

        return False