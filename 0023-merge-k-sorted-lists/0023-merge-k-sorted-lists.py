# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def mergeTwoSortedLinkedLists(head1, head2):
            if head1 is None:
                return head2
            if head2 is None:
                return head1
            dummy = ListNode()
            prevNode = dummy

            while head1 and head2:
                if head1.val < head2.val:
                    prevNode.next = head1
                    head1 = head1.next
                else:
                    prevNode.next = head2
                    head2 = head2.next
                prevNode = prevNode.next
            
            if head1:
                prevNode.next = head1
            
            if head2:
                prevNode.next = head2

            return dummy.next
        
        if len(lists) == 0:
            return None

        for i in range(1, len(lists)):
            lists[0] = mergeTwoSortedLinkedLists(lists[0], lists[i])
        
        return lists[0]