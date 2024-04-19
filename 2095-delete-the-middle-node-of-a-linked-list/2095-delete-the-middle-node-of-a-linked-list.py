# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        """
        Deleting a node means just copy the next node data into current node data until the last but one node is None
        """
        
        if head is None or head.next is None:
            return None
        elif head.next.next is None:
            head.next = None
            return head
        slowPointer, fastPointer = head, head
        while fastPointer is not None and fastPointer.next is not None:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        """ Now we have reached the second middle node of the linked list"""
        while slowPointer.next is not None:
            slowPointer.val = slowPointer.next.val
            if slowPointer.next.next is None:
                slowPointer.next = None
                break
            else:
                slowPointer = slowPointer.next
        return head