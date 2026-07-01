class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # edge case
        if len(nums)<=1:
            return nums
        # find mid
        mid = len(nums)//2
        left=nums[:mid]
        right=nums[mid:]
        # self used because it is a function inside class
        left = self.sortArray(left)
        right = self.sortArray(right)
        result = []
        i=0
        j=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


