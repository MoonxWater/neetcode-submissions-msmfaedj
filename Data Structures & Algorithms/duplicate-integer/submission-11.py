class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums == []:
            return False
        arr = {}
        for num in nums:
            if num not in arr:
                arr.update({num: 1})
                continue
            return True
        return False
            