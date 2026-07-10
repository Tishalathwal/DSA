class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = nums[0]
        max_sum = nums[0]

        i =1
        while i<len(nums):
            current_sum = max(nums[i], current_sum + nums[i])

            if current_sum > max_sum:
                max_sum = current_sum

            i+=1
        return max_sum