# given the dominos, determine the maximum number of removals we can do so that the remaining dominos have a LIS = min_order

# Using a DP approach to start with
class Solution:
    def determineMaximumRemovals(self, domino, remove, min_order):
        removals = 0
        current_domino = domino.copy()
        
        for i in range(len(remove)):
            if remove[i] >= len(current_domino):  # Prevent out-of-bounds errors
                return removals
            
            current_domino.pop(remove[i])  # Remove element at index remove[i]
            
            lis = self.determineLIS(current_domino)  # Compute LIS after removal
            
            if lis >= min_order:
                removals += 1
            else:
                return removals  # Stop if LIS becomes too small
            
            # 🔹 Adjust indices in remove for future iterations
            for j in range(i + 1, len(remove)):
                if remove[j] > remove[i]:  
                    remove[j] -= 1  # Decrement indices that were after the removed one

        return removals  # Return the total successful removals
        
    def determineLIS(self, nums):
        if len(nums) == 1:
            return 1
        
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp) if dp else 0
    
s = Solution()

domino = [1, 4, 4, 2, 5, 3]
remove = [2, 1, 4, 0, 5, 3]
min_order = 3

res = s.determineMaximumRemovals(domino, remove, min_order)

print(res)