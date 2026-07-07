# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # finding the middle of ll
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        # reversing the second half
        curr = middle
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        # comparing both halves
        left = head
        right = prev

        while right: # used only right as for odd numbered ll, left>right
            if left.val!=right.val:
                return False
            left = left.next
            right = right.next
        return True


            
        
