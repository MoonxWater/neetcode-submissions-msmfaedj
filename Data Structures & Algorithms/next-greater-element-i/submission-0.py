class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    found = True
                elif found and nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    break
                
            else:
                res.append(-1)


        return res