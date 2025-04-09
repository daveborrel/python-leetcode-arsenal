class Solution:
    def calculateMaxQualityScore(self, impactFactor, ratings):
        
        initial_sum = self.maximumSubarray(ratings)
        
        if impactFactor == 1:
            return initial_sum
        
        if initial_sum > 0:
            return initial_sum * impactFactor
        else:
            return int(initial_sum / impactFactor)     
    
    def maximumSubarray(self, nums):
        dp = [0] * len(nums)
        
        for i in range(len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)

s = Solution()
impactFactor = 2  
ratings = [5, -3, -3, 2, 4]  
res = s.calculateMaxQualityScore(impactFactor, ratings)
print(res)