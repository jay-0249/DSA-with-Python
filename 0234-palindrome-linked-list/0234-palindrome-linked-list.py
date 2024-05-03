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
        if head is None or head.next is None:
            return True

        slowPointer = fastPointer = head
        #Find the middle node in case of ODD number of nodes
        #Find the first middle node in case of even number of nodes 
        while fastPointer.next and fastPointer.next.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        
        #middleNode = slowPointer
        #secondHalf = slowPointer.next
        #slowPointer.next = None -> not required
        prevNode = None
        currentNode = slowPointer.next
        #Break the second half after the middle or first middle node and Reverse the second Half
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        
        head2 = prevNode
        head1 = head
        #Now iterate over the first half and second half of the linked lists and check their values match
        while head1 and head2:
            if head1.val == head2.val:
                head1 = head1.next
                head2 = head2.next
            else:
                return False
        
        return True
        
