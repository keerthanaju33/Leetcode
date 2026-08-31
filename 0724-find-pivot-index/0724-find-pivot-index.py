class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        leftsum=0
        n = len(nums)
        for i in range(0,n):
            rightsum = total - leftsum - nums[i]
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        return -1
        