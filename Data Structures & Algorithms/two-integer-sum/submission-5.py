class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        arr = {}

        for i in range(len(nums)):
            arr[target - nums[i]] = i

        for j in range(len(nums)):
            if nums[j] in arr.keys() and arr.get(nums[j]) != j:
                return [j, arr.get(nums[j])]
            
        return []