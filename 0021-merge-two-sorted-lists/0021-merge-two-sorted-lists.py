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
        #I want to merge a list into the other list
        #so I will check if either list 1 or list 2 is empty
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        #Now list1 None or list2 None or both empty case are handled
        #Now I will compare list2 head with list1 head, if list2 head element is lesser than I will consider list2 as my primary list
        primaryList, secondaryList = list1, list2

        if list2.val < list1.val:
            primaryList, secondaryList = list2, list1
        
        primaryListHead = primaryList
        
        #If current head of secondary node is less than the next node of the primary list, insert the current secondary head node as the next node of the primary Node
        while primaryList.next and secondaryList:
            if secondaryList.val < primaryList.next.val:
                temp1 = primaryList.next
                primaryList.next = secondaryList
                secondaryList = secondaryList.next
                primaryList = primaryList.next
                primaryList.next = temp1
            else:
                primaryList = primaryList.next
        
        if primaryList.next is None:
            primaryList.next = secondaryList
        
        return primaryListHead
