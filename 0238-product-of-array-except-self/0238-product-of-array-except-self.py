class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        productArr = [1]*len(nums)

        prefixProduct = 1

        for i in range(1,len(nums)):
            prefixProduct *= nums[i-1]
            productArr[i] = prefixProduct
        
        postfixProduct = 1

        for i in range(len(nums)-2,-1,-1):
            postfixProduct *= nums[i+1]
            productArr[i] *= postfixProduct

        return productArr 