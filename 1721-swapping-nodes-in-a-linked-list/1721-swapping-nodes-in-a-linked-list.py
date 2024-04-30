# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        '''
        Two Pointer
        Reach Nth node from the start using first pointer, copy the node temporarily
        Now start iterating using a second pointer to reach the Nth node(from last) while continuing first pointer also to iterate.
        When first pointer hits the last node, second pointer hits the node that is Nth node from the last.
        Time Complexity: O(N)
        Space Complexity: O(1)

        Edge case if N is greater than the length of the linked list
        NOTE: we are reach Nth node rather than N-1 or N+1 node as we just have to swap the values, for which we do not need to swap or skip 
        ( i.e, no change of links - unlink and change links) rather just swap the values
        NOTE: For comparing values, DON'T USE 'is' , rather use '=='
                'is' operator checks for identity rather than equality.
                i.e, 'is' operator checks if the two variables are pointing at the same memory
        '''

        firstPointer = secondPointer = head
        #The problem suggest indexing from one
        nodeIndex = 1

        while nodeIndex<k and firstPointer.next:
            firstPointer = firstPointer.next
            nodeIndex += 1
        print(nodeIndex, k)
        #Length of the linked list is < n
        if nodeIndex != k:
            print(nodeIndex, k)
            print("Struck in edge")
            return head
        print("Crossed edge")
        nodeNfromBegining = firstPointer

        #Now let's use second pointer to reach the Nth node(from the last)
        while firstPointer.next:
            firstPointer = firstPointer.next
            secondPointer = secondPointer.next
            nodeIndex += 1

        #Swap the values of Nth node from the begining and end
        nodeNfromBegining.val, secondPointer.val = secondPointer.val, nodeNfromBegining.val
            
        return head
