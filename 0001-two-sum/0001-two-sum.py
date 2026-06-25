class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in hashmap:
                return [hashmap[needed], i]

            hashmap[num] = i
        