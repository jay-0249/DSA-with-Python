# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #EdgeCases
        if head == None:
            return head
        
        #Base Condition
        prevNode = None
        currNode = head
        nextNode = currNode.next

        #first node reversal
        currNode.next = prevNode

        #Iterative approach until your nextNode is None
        while nextNode:
            #move current node to next node, accordingly nextNode and prevNode are moved
            prevNode = currNode
            currNode = nextNode
            nextNode = nextNode.next
            #Link the currNode's next node to prevNode
            currNode.next = prevNode
        
        return currNode

        
