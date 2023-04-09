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
        one = two = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                one.next = list1
                list1, one = list1.next, list1
            else:
                one.next = list2
                list2, one = list2.next, list2
                
        if list1 or list2:
            one.next = list1 if list1 else list2
            
        return two.next
