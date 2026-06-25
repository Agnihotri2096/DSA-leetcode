class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        present = set()
        for i in nums:
            if i in present:
                return True
            else:
                present.add(i)
        return False