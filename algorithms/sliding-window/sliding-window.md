# Sliding Window

### General Structure

```
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