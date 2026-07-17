class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        while i<n:
            j = nums[i]-1
            if 1<=nums[i]<=n and nums[j]!=nums[i]:
                nums[i],nums[j]= nums[j], nums[i]

            else:
                i+=1

        for i in range(n):
            if nums[i]!= i+1:
                return i+1

        return n+1