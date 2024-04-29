# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        '''
        We do not have the node previous to the node to be deleted, we cannot delete this node by unlinking the node to be deleted.
        Rather we can move the values 
        '''
        currentNode = node
        
        while currentNode.next:
            currentNode.val = currentNode.next.val
            if currentNode.next.next:
                currentNode = currentNode.next
            else:
                break
        currentNode.next = None

        return
        