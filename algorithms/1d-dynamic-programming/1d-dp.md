# 1D - Dynamic Programming

Dynamic Programming helps us solve problems by relating it to smaller subproblems.

Common Question Attributes that make this more likely to be DP:
- Asking for the maximum or minimum of something
- Making decisions based on previous decisions

Imagine a game where you have a n x m grid starting on any tile in the top row moving down.
You have three ways to move:
- directly below
- diagonal down right
- diagonal down left

This recurrence describes the relationship of any coordinate (i,j) with the points that came before it.
- At each point (i, j), what's the maximum points I could have accumulated to reach this position? This is why you look at the points before it.

![image](/algorithms/1d-dynamic-programming/assets/DP-1.JPG)

## General Structure to these types of problems

1. Need a function/array that represents the answer to the problem from a given state.
2. Recurrence Relation - A way to transition between the states.
3. Base Case.

### Examples of these questions.

Using [LeetCode 300: Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/) as an example:

1. We'll setup `dp = [1,1,1]` which represents the LIS that ends with the ith element.
2. If we know everything prior to dp[3], then if nums[3] > nums[2] we just take the LIS at 2 (dp[2]) and then add nums[3] to it.
    - This explains why we decide between the maximum between dp[3] or d[2] + 1
3. The LIS on each element alone is 1

Using [LeetCode 53: Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

1. `dp = [0, 0, 0]` will represent the maximum value of the subarray that ends at index i.
2. dp[i] = max(nums[i], nums[i] + dp[i-1])
    - Either you use the value of the number itself, or add it to the values before it.
    - This is the main reason why we can't use the greedy approach because we can't simply 
    ignore the negative values because adding the negative could result in a larger value.
3. The base case is 0 as initiated in the original dp array

Usign [Coin Change](https://leetcode.com/problems/coin-change/description/)

1. The DP array represents the minimum number of coins at that coin amount. The default value will be `amount + 1` because you might not be able to make a combination.
2. dp[i] = min(dp[i], dp[i-coin] + 1) for coin in coins.
    - To avoid running into an IndexError we check if coin > i before doing the comparison.
3. base case is 0.

## Comparison with Greedy Approaches

Its easy to confuse the two because they both break down the larger problem into smaller ones.

Greedy Approach - Will take the best solution at each step but miss the global solution.

Dynamic Programming - Uses the results of smaller subproblems to solve large problems.