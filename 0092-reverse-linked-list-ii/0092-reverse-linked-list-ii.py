# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        #Adjust left, right to indices
        left -= 1
        right -= 1
        #Edge case handling
        if left>=right or head is None:
            return head 
        if left < 0:
            left = 0
        #Iterate untill you reach the Node until the index = left
        index = 0
        #Find the node with index = left
        currentNode = head
        while currentNode and index < left-1:
            currentNode = currentNode.next
            index += 1
        #Store the node at index = left-1 and the node at index = left
        #Handle the scenario head is the node at index = left
        if left>0:
            leftPrevNode = currentNode
            leftNode = currentNode.next
        else:
            leftPrevNode = None
            leftNode = head
        #Break if there is no node at index = left or index = left + 1 (if we do not have any Node available  after the node at index = left, we do not have to reverse anything)
        if leftNode is None or leftNode.next is None:
            return head
        #Now start reversing from the node at index = left until you reach the None or node at index = right
        prevNode = None
        currentNode = leftNode
        index = left
        print(currentNode, "before reversal")
        while currentNode and index < right+1:
            print(currentNode)
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
            index += 1
        #Connect the reversed linked list between indices = left & right with the rest of the linked list
        leftNode.next = currentNode
        #Handle the scenario head is the node at index = left
        if left > 0:
            leftPrevNode.next = prevNode
            return head
        else:
            return prevNode

            