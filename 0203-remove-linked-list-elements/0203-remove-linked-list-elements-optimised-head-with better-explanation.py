# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prevNode = head
        if head:
            currentNode = head.next
        else:
            return head
        #If the current node value matches with the input value, remove the current node
        while currentNode:
            if currentNode.val == val:
                prevNode.next = currentNode.next
            else:
                prevNode = currentNode
            currentNode = currentNode.next
        #Check the first node
        if head and head.val == val:
            head = head.next
        return head
        