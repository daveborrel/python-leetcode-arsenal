# Backtracking

- Uses brute force to solve problems. If the current solution is not valid, then backtrack and find other solutions.

##  General Structure

```

Backtrack(x)
    if x is not solution:
        return false
    if x is a new solution:
        add to the list of solutions
    Backtrack(expand x)
```

## Types of Questions

### Subsets Backtracking Pattern

```
SubsetBacktrack(index):
    # Base case - we've processed all numbers
    if index == len(nums):
        add current_subset to solutions
        return
    
    # Decision 1: Include current number
    add nums[index] to current_subset
    SubsetBacktrack(index + 1)   # Always move forward
    
    # Decision 2: Don't include current number
    remove nums[index] from current_subset
    SubsetBacktrack(index + 1)   # Always move forward
```

### Combination Sum Backtracking Pattern


```
CombinationBacktrack(index):
    # Base cases
    if current_sum == target:
        add current_combination to solutions
        return
    if current_sum > target or index >= len(nums):
        return
    
    # Decision 1: Include current number (can reuse)
    add nums[index] to current_combination
    CombinationBacktrack(index)   # Stay at same index
    
    # Decision 2: Don't include current number
    remove nums[index] from current_combination
    CombinationBacktrack(index + 1)   # Move to next number
```
