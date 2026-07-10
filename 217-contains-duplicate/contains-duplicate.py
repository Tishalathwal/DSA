class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        i=0
        while i<len(nums):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])
            i+=1
        return False
        