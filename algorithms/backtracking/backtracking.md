# Backtracking

- Uses brute force to solve problems. If the current solution is not valid, then backtrack and find other solutions.

Using a visual example here:

- We'll start at S, and then work our way towards S1. If its not valid, then we backtrack into M1 and then S, and then subsequently working our way towards the other solutions in the space.

![image](/algorithms/backtracking/assets/algorithms.JPG)



##  General Structure

```python
# we'll use a list for this example, but could be anything (string, number, etc)
candidate = []

def backtrack(x)
    if x is not solution:
        # return false
    if x is a new solution:
        # add to the list of solutions
    
    # update candidate and then call backtrack
    candidate.append()
    backtrack(x + 1)

    # remove what you added to allow backtracking
    candidate.pop()

```


## Types of Questions

### Subsets Backtracking Pattern

- In this problem you always 

```python
def SubsetBacktrack(index):
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


```python
def CombinationBacktrack(index):
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

### Generate Parenthesis

- We use two different counts here because it ensures that the string generated is valid.

```python
def dfs(index):

    # base case
    if lc + rc == 2*n:
        # add to result array
    
    # decision 1
    if lc < n:
        # add an open parenthesis to the current substring
        dfs(lc + 1, rc)
        # remove open parenthesis

    # decision 2
    if lc > rc:
        # add a close parenthesis to the current substring
        dfs(lc, rc + 1)
        # remove open parenthesis
```

### References for Images

https://www.simplilearn.com/tutorials/data-structure-tutorial/backtracking-algorithm 
