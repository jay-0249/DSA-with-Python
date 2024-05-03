# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        1st approach
        Copy all the node values into a array
        Then check if it is a palindrome
        Time Complexity -> O(N)
        Space Complexity -> O(N)

        2nd Approach
        Find the middle element, then at the middle node reverse the second half of the linked list.
        Then iterate to compare both lists if their values are same
        Time Complexity -> O(N)
        Space Complexity -> O(1)
        '''
        nodeArray = []
        currentNode = head
        #Push node to array
        while currentNode:
            nodeArray.append(currentNode.val)
            currentNode = currentNode.next
        
        #Now iterate over the linked list from head and array from last
        #See if the values match, if not it is not palindrome
        currentNode = head
        i = len(nodeArray)-1
        while currentNode:
            #Return false if the if the value at kth Node from start and end do not match
            if currentNode.val != nodeArray[i]:
                return False
            else:
                currentNode = currentNode.next
                i -= 1

        return True