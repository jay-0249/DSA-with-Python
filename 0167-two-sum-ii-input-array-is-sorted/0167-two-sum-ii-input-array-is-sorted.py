class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_index = 0
        right_index = len(numbers) - 1

        while left_index < right_index:
            sum = numbers[left_index] + numbers[right_index]
            if sum == target:
                return [left_index+1, right_index+1]
            elif sum>target:
                right_index -= 1
            else:
                left_index += 1
        
        return [left_index+1, right_index+1]