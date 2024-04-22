# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        prev -> current -> next
        prev <- current, next
        Now move to next node, assign prevNode = currentNode,
                                      current = nextNode
        start with prevNode as None and currentNode as head continue until currentNode is None
        """
        #head is directly used for memory optimisation, but using curretNode would be a safer choice
        prevNode = None
        while head:
            nextNode = head.next
            head.next = prevNode
            prevNode = head
            head = nextNode

        return prevNode
        