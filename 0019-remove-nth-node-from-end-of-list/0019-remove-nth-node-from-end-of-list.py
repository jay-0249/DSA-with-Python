# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        '''
        1st approach
        Count the number of nodes in the linked list by iterating through the linked list.
        Now iterate from head to reach the node that is just before the Nth node(from last).
        Skip that node. Return head

        2nd approach
        Have two pointers. Let the first pointer reach N-1 nodes
        Then along with 1st pointer continuing iteration to reach last node, let 2nd pointer will start to iterate from head to reach the N+1 node(from last).
        Skip that node. Return head 

        TimeComplexity -> O(N)
        SpaceComplexity -> O(1)

        Edge case: 1. Head is the node to be removed
                   2. The length of the linked list is less than n i.e, we do not a node in the linked list that is Nth node from the last node  
        '''
        if head is None:
            return head

        firstPointer = secondPointer = head
        #nodeIndex indicates the index of the node firstPointer points at a moment
        nodeIndex = 0
        #Iterate until the first pointer reaches node with index 'n'
        while nodeIndex<n and firstPointer.next:
            firstPointer = firstPointer.next
            nodeIndex += 1
        #Check if we still did not hit the last node - real life scenario - not required for this problem
        if firstPointer:
            #Now iterate until second pointer from head reaches the node that is previous to Nth node(from last)
            while firstPointer.next:
                firstPointer = firstPointer.next
                secondPointer = secondPointer.next
                nodeIndex += 1
        #If the node to removed is the head, as we do not have a previous node to head node, just return the node next to head
        if nodeIndex is n-1:
            return head.next
        if secondPointer.next:
            secondPointer.next = secondPointer.next.next
        
        return head