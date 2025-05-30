class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        tempSum = 0
        for i in range(len(nums)):
            if tempSum < 0:
                tempSum = 0
            tempSum += nums[i]
            
            maxSum = max(maxSum, tempSum)
        return maxSum
