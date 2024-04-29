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
        #Check if the Node to the deleted is the Last Node
        if currentNode.next:
            #If we have a node next to next to currentNode
            while currentNode.next.next:
                #Move the value of next node to this node
                currentNode.val = currentNode.next.val
                currentNode = currentNode.next
            #Last node val to be transferred 
            currentNode.val = currentNode.next.val
            currentNode.next = None

        return
        