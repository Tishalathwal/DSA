class Solution(object):
    def rotate(self, nums, k):

        n = len(nums)
        k = k % n

        temp = [0] * n

        for i in range(n):
            temp[(i + k) % n] = nums[i]

        for i in range(n):
            nums[i] = temp[i]
