class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # if nums[-1] != len(nums):
        #     return len(nums) 
        # for i in range(len(nums)):
        #     if nums[i] != i:
        #         return i
        # return 0

        return sum(range(len(nums)+1)) - sum(nums)