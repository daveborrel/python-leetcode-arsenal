
"""
Problem: Find Target or Closest Number in Sorted Array

Given a sorted array of integers and a target value, find the target in the array.
If the target is not present, return the closest number to the target in the array.

Example 1:
Input: nums = [1, 3, 5, 7, 9], target = 5
Output: 5
Explanation: Target 5 is found in the array.

Example 2:
Input: nums = [1, 3, 5, 7, 9], target = 6
Output: 5 or 7
Explanation: Both 5 and 7 are equally close to target 6 (difference of 1).
For this case, you can return either one.

Example 3:
Input: nums = [1, 3, 5, 7, 9], target = 10
Output: 9
Explanation: Target 10 is not in the array. The closest number is 9.

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
-10^4 <= target <= 10^4
nums is sorted in ascending order.
"""

# this is some sort of binary search problem, to where if we don't have the value present, we just find the closest one.
# store that middle value.
# what if 5 and 7 are equally apart.
# nums = [1, 3, 5, 7, 9]

def find_target(nums, target):
    
    res = float('inf')
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        
        if target == nums[mid]:
            return nums[mid]
        elif target < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
            
        curr_diff = abs(target - nums[mid])
        res_diff = abs(target - res)
        
        if curr_diff < res_diff:
            res = nums[mid]
    
    return res

n1 = [1, 3, 5, 7, 9] 
t1 = 5

print(find_target(n1, t1))

n2 = [1, 3, 5, 7, 9]
t2 = 6

print(find_target(n2, t2))

n3 = [1, 3, 5, 7, 9] 
t3 = 10

print(find_target(n3, t3))