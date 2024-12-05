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
        
        prevNode, currentNode = None, head
        
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode

        return prevNode
        
