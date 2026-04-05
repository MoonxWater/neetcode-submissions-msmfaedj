class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        arr = {}

        for i in range(len(nums)):
            arr[target - nums[i]] = i

        for i in range(len(nums)):
            if nums[i] in arr and arr.get(nums[i]) != i:
                return [i, arr.get(nums[i])]
            
        return []