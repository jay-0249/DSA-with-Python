class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        nums1CurrentIndex = m-1
        nums2CurrentIndex = n-1
        nums1InsertAtIndex = n+m-1
        
        while nums2CurrentIndex>-1 and nums1CurrentIndex>-1:
            if nums2[nums2CurrentIndex]>nums1[nums1CurrentIndex]:
                nums1[nums1InsertAtIndex] = nums2[nums2CurrentIndex]
                nums2CurrentIndex -= 1
                nums1InsertAtIndex -= 1
            else:
                nums1[nums1InsertAtIndex] = nums1[nums1CurrentIndex]
                nums1CurrentIndex -= 1
                nums1InsertAtIndex -= 1
        
        while nums2CurrentIndex>-1:
            nums1[nums1InsertAtIndex] = nums2[nums2CurrentIndex]
            nums2CurrentIndex -= 1
            nums1InsertAtIndex -= 1
        
        while nums1CurrentIndex>-1:
            nums1[nums1InsertAtIndex] = nums1[nums1CurrentIndex]
            nums1CurrentIndex -= 1
            nums1InsertAtIndex -= 1

        return