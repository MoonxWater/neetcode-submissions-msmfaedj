class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        '''
        temp = []
        left = 0
        right = 0

        while left < m and right < n
        if nums1[left] <= nums2[right]:
            take nums1[left] and left++

        else take nums2[right] and right++

        nums1[:] = temp[:]
        '''

        temp = []
        left = right = 0

        while left < m and right < n:
            if nums1[left] <= nums2[right]:
                temp.append(nums1[left])
                left += 1
            else:
                temp.append(nums2[right])
                right += 1
        
        temp.extend(nums1[left:m])
        temp.extend(nums2[right:n])
        nums1[:] = temp[:]

        



        
        