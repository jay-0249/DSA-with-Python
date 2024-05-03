# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        '''
        We always have even number of nodes
        Reverse the nodes until first middle node including the first middle node. So we have to combine both finding the first middle node and revsering the nodes
        Then iterate over the both halfs of the linked list to find the maximum sum of twin nodes
        Time Complexity -> O(N)
        Space Complexity -> O(1)
        '''
        if head is None:
            return 0

        slowPointer = fastPointer = head
        prevNode = None
        #Reverse the nodes till first middle node, including the first middle node
        while fastPointer and fastPointer.next:
            fastPointer = fastPointer.next.next
            nextNode = slowPointer.next
            slowPointer.next = prevNode
            prevNode = slowPointer
            slowPointer = nextNode
        
        head1 = prevNode
        head2 = slowPointer

        maxTwinNodeSum = head1.val + head2.val
        #Iterate over both halfs of Linked lists to find the maximum twin node sum
        while head1 and head2:
            currentTwinNodeSum = head1.val + head2.val
            if currentTwinNodeSum > maxTwinNodeSum :
                maxTwinNodeSum = currentTwinNodeSum
            head1 = head1.next
            head2 = head2.next
        
        return maxTwinNodeSum


