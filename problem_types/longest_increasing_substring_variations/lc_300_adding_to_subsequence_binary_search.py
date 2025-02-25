class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int: 

        # create a subsequence with the 
        sub = [nums[0]]

        for num in nums:

            i = bisect_left(sub, num)

            # meaning the left insertion point we got was outside of the existing subsequence
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
            
        return len(sub)