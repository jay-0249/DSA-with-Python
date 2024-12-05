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
        #Base Condition
        prevNode, currNode = None, head

        #Iteratively reverse the current node's next pointer to previous node
        while currNode:
            nextNode = currNode.next   #store next node
            currNode.next = prevNode   #point the link of next node to prev node 
            prevNode = currNode        #shift prev node
            currNode = nextNode        #shift curr node
        
        #return the last node as head
        return prevNode