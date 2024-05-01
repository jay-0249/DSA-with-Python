# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        '''
        Iterate over the first linked list and Store the nodes of the first linked list in set.
        Then iterate over second linked list and see if any node matches, return that node.

        NOTE: we are using set as the time for searching an element is almost O(1)

        space complexity -> O(A)
        Time Complexity -> O(A + B)
        '''
        #Create a set
        nodeSet = set()
        currentNode = headA
        #Iterate over the linked list A and store the nodes
        while currentNode:
            nodeSet.add(currentNode)
            currentNode = currentNode.next
        
        currentNode = headB
        #Iterate over the linked list B and check if any node of B matches with a node in set
        while currentNode:
            if currentNode in nodeSet:
                return currentNode
            else:
                currentNode = currentNode.next
        
        return None