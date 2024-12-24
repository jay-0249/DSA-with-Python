from collections import deque
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
        #we can use stack to store the first half of the node values
        #we can use slow and fast pointer technique to find the middle node
        slowPointer, fastPointer = head, head
        firstNNodes = deque()
        
        while fastPointer:
            #store the first N node values
            firstNNodes.append(slowPointer.val)
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next #we are directly going for next to next node without chceking because the constraints state that the linked list is of even length

        #then we can iterate over the second half of the linked list
        #use a global variable to store the maximum twin sum
        max_twin_sum = 0
        while slowPointer:
        #to find the twin sum for each of the node
            twin_sum = slowPointer.val + firstNNodes.pop()
            if max_twin_sum < twin_sum:
                max_twin_sum = twin_sum
            slowPointer = slowPointer.next
        
        return max_twin_sum
        