# Sliding Window

This is a probelm solving technique use to help us with a variety of different problems.
- Running average, formulating adjacent pairs, target value identification, longest/shortest sequence

Benefit of using a sliding window reduces the time complexity of O(n^2) into O(n)

### General Structure

- Need to Start using `start` and `end` for window size labels.

#### Fixed Window Pseudocode

Method 1 - `while end < len(arr)`
- Starts with both pointers at the first element
- While end is less than the length of the array
    - Add the value at the end pointer
    - If size of the window is larger than what is valid, then remove element
    - If size of window is equal to k
    - If not, then we increase the size of the window

[Example In LeetCode 567](/algorithms/sliding-window/lc-567-permutation-in-string-template.py)

```python
def fixed_window_while_modifying_size_concurrently(sequence, k):
    start, end = 0, 0
    window_size = k

    while end < len(sequence):
        
        add to window
        
        if end - start + 1 > k:
            #reduce window
            start += 1
        
        if end - start + 1 == k:
            # check if it satisfies the answer
```


Method 2 - `for end in range(len(arr))`
- In this version you instantiate your window and then check its size.
- You can then use a for loop to start sliding the window down
- However, its a bit less readable without `start` and `end` pointers.

[Example In LeetCode 567](/algorithms/sliding-window/lc-567-permutation-in-string-for-loop.py)

```python
def fixed_window_after_checking_it_first(sequence, k):
    window_size = k

    Initialize first window - will only need one pointer
    Check first window

    for i in range(whereever that first window ended + 1, length of sequence):
        add new element to window
        remove old element
        check if the answer fits
```

For Method 2, there is a way to use a start and end pointer to make it more explicit.

[Example In LeetCode 567](/algorithms/sliding-window/lc-567-permutation-in-string-initialization.py)


#### Variable Window Psudocode

```python
def variable_window_size(sequence):
    start, end = 0, 0
    while end < len(sequence):

        if (end - start + 1 < k):

            # Expand the window until desired window size is reached

            end += 1
        elif (end - start + 1 == k):

            # Perform calculations and store the answer in the variable

            end += 1
        else:
            while (end - start + 1 > k):

                # Shrink window while its larger than the intended size
                
                start += 1
            
            if (end - start + 1 == k):

                # Do calculations to check if its the answer you window_start

            end += 1
    return ans
```



```python
def sliding_window_template(arr):
    # 1. Initialize window variables
    window_start = 0
    window_sum = 0  # or other window state
    result = 0  # or other result variable
    
    # 2. Extend the window with window_end
    for window_end in range(len(arr)):
        # 3. Add element at window_end to your window state
        window_sum += arr[window_end]
        
        # 4. If condition to shrink window (e.g., size check)
        while CONDITION:
            # 5. Remove element at window_start from window state
            window_sum -= arr[window_start]
            window_start += 1
            
        # 6. Update result if needed
        result = max(result, window_end - window_start + 1)
    
    return result
```


### Sources

[Leetcode Article on this topic](https://leetcode.com/discuss/interview-question/3722472/mastering-sliding-window-technique-a-comprehensive-guide)