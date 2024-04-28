# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        1st approach  - using set
            As we iterate, we check the nodes if it is in set else we add the node the node to the set
            If the current node is in the set then it means we are visiting that node again. So we have a cycle in linked list.
            Time Complexity - O(N)
            Space complexity - O(N)

        2nd approach - using two pointer (slow and fast)
            As we iterate over the linked list, if the fast pointer meets the slow pointer, we have a cycle in the linked list
            Time Complexity - O(N)
            Space complexity - O(1)
        '''
        nodeSet = set()

        slowPointer, fastPointer = head, head

        while fastPointer and fastPointer.next:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            if fastPointer is slowPointer:
                return True

        return False
