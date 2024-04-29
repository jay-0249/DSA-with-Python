# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #Check if any list is empty
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        head = None
        #Assign the head
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        #prevNode will be helpful to link node with next smallest number
        prevNode = head
        #prevNode will always not be None. Check if list1 node or list2 node is None.
        while list1 and list2:
            if list1.val<list2.val:
                prevNode.next = list1
                list1 = list1.next
            else:
                prevNode.next = list2
                list2 = list2.next
            prevNode = prevNode.next
            
        prevNode.next = list1 if list1 else list2

        return head