class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0

        for num in nums:
            answer ^= num

        return answer

        