# Binary Search

This is a searching algorithm for finding an element's position in a sorted array.
If the array is not sorted, then you would need to sort the array.

### Basic Structure

In general, you setup two pointers `low` / `high` or `left` or `right` 

and then find the middle position: `mid = (left + right) // 2`
- Remember that in python you have to use `//` for integer division.

![image](/algorithms/binary-search/assets/binary%20search.JPG)

### Importance of the terminating condition when using a while loop.

The main difference between `while l < r` and `while l <= r` lies in whether the loop includes the case where l == r.

`while l <= r`
- Checks all of the indices including `l == r`
- Using the other version might miss cases where `nums[mid] == target`

### variations