# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        1st approach
        copy all the node values into an array
        sort the array
        copy back the values into the nodes
        Time Complexity -> O(nlogn)
        Space Complexity -> O(n)

        2nd Approach
        Use merge sorting
        Break the linked list into two halfs, use recursion and follow merge sort
        Again join the sorted halfs of linked lists
        Time Complexity -> O(N)
        '''

        if head is None or head.next is None:
            return head
        
        slowPointer = fastPointer = head
        #Reach the middle node (odd of nodes)
        #Reach the first middle node (even of nodes)
        while fastPointer.next and fastPointer.next.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        
        #Sort left half and right half of the linked lists seperately
        rightHalf = self.sortList(slowPointer.next)
        #Unlink the left half of the linked list with the right half of the linked list 
        slowPointer.next = None
        leftHalf = self.sortList(head)

        #Merge the sorted linked lists
        dummy = ListNode()
        prevNode = dummy
        while leftHalf and rightHalf:
            if leftHalf.val < rightHalf.val:
                prevNode.next = leftHalf
                leftHalf = leftHalf.next
            else:
                prevNode.next = rightHalf
                rightHalf = rightHalf.next
            prevNode = prevNode.next
        
        if leftHalf:
            prevNode.next = leftHalf
        
        if rightHalf:
            prevNode.next = rightHalf

        return dummy.next


        