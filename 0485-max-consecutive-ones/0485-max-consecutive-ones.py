class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        curr =0
        maxi = 0
        for num in nums:
            if num == 1:
                curr+=1
                maxi = max(curr,maxi)
            else:
                curr= 0
        return maxi