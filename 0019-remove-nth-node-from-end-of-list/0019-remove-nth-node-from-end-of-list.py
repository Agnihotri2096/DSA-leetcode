# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # need dummy node for if only 1 element in linked list
        dummy = ListNode(0)
        dummy.next = head
        # Fixed gap two pointer problem
        slow = dummy
        fast = dummy
        # move fast n steps ahead
        for _ in range(n+1):
            fast = fast.next
        # move both pointers together
        while fast:
            fast = fast.next
            slow = slow.next
        # delete node
        slow.next = slow.next.next
        return dummy.next


