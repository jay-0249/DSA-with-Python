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
        Rather we can copy the next node val to the node to be deleted. We can skip next node in the linked list sequence
        We do not need to move the values of all nodes - Optimisation
        Time Complexity -> O(1)
        Space Complexity -> O(1)

        If we move the values of all nodes.
        Time Complexity -> O(N)
        Space Complexity -> O(1)
        '''
        currentNode = node
        #Check if the Node to the deleted is the Last Node
        if currentNode.next:
                #Move the value of next node to this node
                currentNode.val = currentNode.next.val
                #Skip the next node in the linked list sequence
                currentNode.next = currentNode.next.next

        return
        