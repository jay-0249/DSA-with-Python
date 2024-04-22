class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        """
        Reverse the string by swapping the characters of the list using two pointer
        swap kth character from start with kth character from end until no swap is required
        """
        start = 0
        end = len(s)-1
        while start<end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1
        return s