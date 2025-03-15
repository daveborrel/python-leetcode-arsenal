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

- Each number is either chosen, or omitted which explains why the index increases each time.

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

- Each number could potentially be used multiple times. This explains why the recursion goes as deep as it can with repeated numbers before exiting to the next number.

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

- Two different counts here because it ensures that the string generated is valid.

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

### Combination Sum II

- An extension of combination sum.
- Need to cover the case of duplicate answers
- Need to reduce the use of sum() and calculate the sum as you are traversing the different possibilities.

Note on recursion
- `if i > idx and candidates[i] == candidates[i - 1]:` 
- The purpose of this line prevents duplicate numbers at the same recursion level
    - recursion level 1 with `path = [1]`
        - this will explore all combinations excluding `path = [1,1]` because we've already explored that in a deeper level
    - recursion level 2 with `path = [1, 1]`
        - we explore all possible combinations starting with `path = [1,1]`
    - Even more context
        - Lets say we had `candidates = [1,1,1,2,5,6,7]`
        - This means that at recursion level 3, we'll have `path = [1,1,1]`
            - so by the time we exit into recursion level 2, we'll skip out on `path = [1,1,1]` because its been done before.


```python
        def dfs(idx, path, cur):
            if cur == target:
                res.append(path.copy())
                return
            for i in range(idx, len(candidates)):
                # checks if duplicate for that level of recursion.
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if cur + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i + 1, path, cur + candidates[i])
                path.pop()
```

### Additional Sources
[Leetcode Explore Card](https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2654/)


### References for Images

https://www.simplilearn.com/tutorials/data-structure-tutorial/backtracking-algorithm 
