class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # this is a simple approach but two pointer approach is accepted here
        '''s[:] = s[::-1]'''
        #two pointer approach
        left = 0
        right = len(s) - 1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left +=1
            right-=1
