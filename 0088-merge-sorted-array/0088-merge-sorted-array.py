class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        b = n-1
        a = m-1
        k = m+n-1

        while b>-1:
            if nums2[b] >= nums1[a]:
                nums1[k] = nums2[b]
                b -= 1 
            else:
                nums1[k] = nums1[a]
                a -= 1
            k -= 1
        return 