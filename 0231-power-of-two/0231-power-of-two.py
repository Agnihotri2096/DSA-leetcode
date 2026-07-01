class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #solved using simple loop earlier
        # now bit manipulation
        return n > 0 and (n & (n - 1)) == 0

            