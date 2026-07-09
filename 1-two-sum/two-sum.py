class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0

        while left < len(nums):

            right = left + 1

            while right < len(nums):

                total = nums[left] + nums[right]

                if total == target:
                    return [left, right]

                right += 1

            left += 1

        return []
        
        