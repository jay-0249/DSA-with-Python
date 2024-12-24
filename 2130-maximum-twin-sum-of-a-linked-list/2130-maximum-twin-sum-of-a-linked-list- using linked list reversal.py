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
        #reverse the first half of the linked list
        prev, slowPointer, fastPointer = None, head, head
        while fastPointer:
            fastPointer = fastPointer.next.next
            next = slowPointer.next
            slowPointer.next = prev
            prev = slowPointer
            slowPointer = next
        #then iterate on both halves of the linked list using two pointers
        #use a variable to store the maximum twin sum
        max_twin_sum = 0
        while slowPointer:
            #at each iteration calculate the twin sum
            twin_sum = slowPointer.val + prev.val
            if max_twin_sum < twin_sum:
                max_twin_sum = twin_sum
            slowPointer = slowPointer.next
            prev = prev.next
        
        return max_twin_sum