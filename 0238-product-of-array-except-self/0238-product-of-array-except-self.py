class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        Iterate over the array, at each iteration use a increment prefix product starting from index 1
        similarly iterate from lastr but one element of the array in the similar approach of incremental product to calculate postfix product
        '''
        prefix_product = 1
        product = [1]*len(nums)
        
        for i in range(0,len(nums)-1):
            prefix_product *= nums[i]
            product[i+1] = prefix_product

        postfix_product = 1
        for i in range(len(nums)-2,-1,-1):
            postfix_product *= nums[i+1]
            product[i] *= postfix_product

        return product 