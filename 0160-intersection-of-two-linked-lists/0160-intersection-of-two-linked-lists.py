# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        hash = set()
        curr = headA
        while curr:
            hash.add(curr)
            curr = curr.next
        currB = headB
        while currB:
            if currB in hash:
                return currB
            currB = currB.next
        return None

