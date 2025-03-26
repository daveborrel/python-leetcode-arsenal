# Median of Two Sorted Arrays

This is a tricky question because we aren't allowed to merge the two arrays and then check for the median. You have to do it in place at O(log(m+n)).

## Different Approaches

### NeetCode

``` python
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # ensures that A will always be the smaller one
        if len(B) < len(A):
            A, B, = B, A

        # taking the length of the left half
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # pointer for A
            j = half - i - 2 # pointer for B

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")

            # Partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                
                #even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
```

A confusing part from his solution is initializing i and j.

Lets get a visual of this part of the code using this example.
- A = [1, 2, 3, 4, 5]
- B = [1, 2, 3, 4, 5, 6, 7, 8]
- total length = 13
- half = 6

When we initialize A, we'll get:

```
A:  [1, 2, 3 | 4, 5]
     0  1  2   3  4
           ^
           i = 2
```

Where `left_subarray_of_A = [1,2,3]`

We know that the length of the `left_subarray_of_B` is equal to `half - len(left_subarray_of_A)`. Which should be 6 - 3 = 3. This means that we need 3 elements from B.

So where do we derive `j = half - i - 2` from?

Its more intuitive to think of this first

### `half = (i + 1) + (j + 1)`

- `half` = the total number of elements we need
- `i + 1` = the elements that come from array A, we add 1 because its a 0 based index
- `j + 1` = the elements that come from array B, we add 1 because its a 0 based index

Therefore we can just solve for j.

Which gives us

`j = half - i - 2`

```
B:  [1, 2, 3, 4, 5, 6, 7 | 8]
     0  1  2  3  4  5  6   7
            ^
            j = 2
```