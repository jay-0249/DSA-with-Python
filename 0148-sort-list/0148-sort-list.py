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
        '''
        nodeValues = []
        currentNode = head
        while currentNode:
            nodeValues.append(currentNode.val)
            currentNode = currentNode.next
        
        nodeValues.sort()
        currentIndex = 0
        currentNode = head
        while currentNode:
            currentNode.val = nodeValues[currentIndex]
            currentNode = currentNode.next
            currentIndex += 1

        return head