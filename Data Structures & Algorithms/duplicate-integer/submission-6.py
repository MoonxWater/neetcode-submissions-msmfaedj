class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums == []:
            return False
        arr = {}
        for num in nums:
            if num not in arr:
                arr.update({num: 1})
                continue
            arr[num] += 1
        if max(arr.values()) > 1: return True
        else: return False
            