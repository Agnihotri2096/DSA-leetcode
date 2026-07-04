class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # My thought solution
        '''rang = [num for num in range(len(nums)+1)]
        for num in rang:
            if num not in nums:
                return num '''
        # above solution will have overall complexity of O(n^2)
        # hash set solution with O(n) complexity
        '''seen = set(nums)
        for num in range(len(nums) + 1):
            if num not in seen:
                return num'''
        # xor solution with O(1) complexity
        xor = len(nums)
        for i in range(len(nums)):
            xor ^= i
            xor ^= nums[i]

        return xor

