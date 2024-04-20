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

        # Find the middle of the list
        slowPointer, fastPointer = head, head
        while fastPointer.next and fastPointer.next.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

        # Reverse the second half of the list
        currentNode = slowPointer.next
        prev = None
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = nextNode

        # Detach the second half
        slowPointer.next = None
        secondHalf = prev

        # Merge the two halves
        currentNode = head
        while secondHalf:
            temp = secondHalf.next
            secondHalf.next = currentNode.next
            currentNode.next = secondHalf
            currentNode = secondHalf.next
            secondHalf = temp

        return head
