class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        Approach 1:

        Create an array to store the products.

        Iterate over the array, in each iteration find the product all the numbers before the current number using a product variable. In each Store the products in an array. This way we find the prefix product in O(N) order of time, by iterating from index 1 to last element and using the prefix product variable for calculating the prefix product icrementally.

        Similarly, find the postfix product for each number, by iterating from last but one element to index 0, to incrementally calculate the postfix product. 
        
        Time Complexity O(N)
        Space Complexity O(N)
        '''
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