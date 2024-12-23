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
        #store the first half of the linked list into a list
        firstNNodes = list()
        slowPointer, fastPointer = head, head
        # fast pointer will always be on a node with index of even number, as we have even number of nodes, fast pointer can always directly check if it has a node on next even number index
        while fastPointer:
            firstNNodes.append(slowPointer.val)
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

        #then we can have the slow pointer on the second half of the linked list and a pointer on the list from the end to iterate and find the twin sum
        #we can maintain a variable to store the maximum twin sum
        max_twin_sum = 0
        for i in range(1,len(firstNNodes)+1):
            curr_twin_sum = slowPointer.val + firstNNodes[-i]
            if max_twin_sum < curr_twin_sum:
                max_twin_sum = curr_twin_sum
            slowPointer = slowPointer.next
        
        return max_twin_sum
