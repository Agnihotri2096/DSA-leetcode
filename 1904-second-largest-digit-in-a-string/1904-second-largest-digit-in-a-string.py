class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = set()
        # made a set for only integers
        for i in s:
            if i.isdigit():
                digits.add(int(i))
        #converted set into an array
        digits = list(digits)
        #sorted the array
        sorted = digits.sort()
        #returned second largest
        if len(digits) < 2:
            return -1
        return digits[-2]
                
