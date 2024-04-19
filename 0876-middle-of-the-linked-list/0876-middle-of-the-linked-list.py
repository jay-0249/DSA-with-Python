# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        What do we need?: Second middle node
        Approach: Fast pointer & slow pointer, Loop
        Basic Move: 
            At each iteration, Fast pointer f = (f.next).next
                               Slow pointer s = (s.next)
        Edge Case:
            Slow Pointer will not access null, until fast pointer does not access null
            So if fast pointer does not access null, we will be good
            Head should not be empty
            As we gonna assign fast with a new node in each iteration, we should check if 
            fast. next node is null
        Optimisation:
        check for fastPointer and fastPointer.next is NOT None, after assigning. So that slowPointer is automatically assigned with 2nd middle node if there are two middle nodes, as you are going to check fastPointer or it's next node is None after fastPointer or fastPointer.next becomes None.
        """
        slowPointer, fastPointer = head, head
        while fastPointer is not None and fastPointer.next is not None:
            slowPointer = slowPointer.next
            fastPointer =  fastPointer.next.next
        return slowPointer