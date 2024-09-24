class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1
        #l,r travel towards eachother so we do not require additional condiations over the bounds of l,r
        while l < r:
            sum = numbers[l]+numbers[r]
            if sum == target:
                return [l+1,r+1]
            elif sum < target:
                l += 1
            else:
                r -= 1
        
            