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

### Combination Sum II

- An extension of combination sum where we check for duplicates.

```python
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        def dfs(idx, path):  
            res.append(path[::])        
            
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()
        
        dfs(0, [])
        return res
```

This line: `if i > idx and candidates[i] == candidates[i - 1]:` checks if the current candidate is a duplicate.

This image illustrates the different recursion levels. Each recursion level will check subsets that can be formed with each "duplicate". 
- One recursion level will have `path = [1]`, and another will have `path = [1,1]`

![subsets2_image](/algorithms/backtracking/assets/subsets2.JPG)


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

### Letter Combinations of a phone number
[LC Question 17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)

Generating all the combinations based on an old phone keypad with 9 digits.

```python
        def dfs(curr):
            if curr == len(digits):
                combined = ""
                for c in current_combination:
                    combined += c
                res.append(combined)
                return

            # For each digit, there are 3-4 letters associated with it
            for letter in digit_mapping[digits[curr]]:
                current_combination.append(letter)
                dfs(curr+1)
                current_combination.pop()
```

### Additional Sources
[Leetcode Explore Card](https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2654/)


### References for Images

https://www.simplilearn.com/tutorials/data-structure-tutorial/backtracking-algorithm 
