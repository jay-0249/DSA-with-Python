# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
            return head
        #Find the middle node (odd no. of nodes) or second middle node (even no.  of nodes)
        slowPointer, fastPointer = head, head
        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

        #Reverse the list after the middle or 2nd middle node
        currentNode = slowPointer.next
        prev = None

        while currentNode:
            nextNode = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = nextNode
        #Now detach the middle or second middle node with the second half by assigning slowPointer.next with None
        slowPointer.next = None
        #SecondHalf pointer
        secondHalf = prev
        
        #Now start inserting Ln between L0 and L1 and continue inserting the nodes from array until the second Pointer is None
        currentNode = head
        while secondHalf:
            lastNode = secondHalf
            secondHalf = secondHalf.next
            firstHalfNext = currentNode.next
            lastNode.next = firstHalfNext
            currentNode.next = lastNode
            currentNode = firstHalfNext
        return head

