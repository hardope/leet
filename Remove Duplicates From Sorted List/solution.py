# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        while node is not None:
            cur = node.val
            try:
                if node.next.val == cur:
                    node.next = node.next.next
                else:
                    node = node.next
            except:
                node = node.next

        return head
