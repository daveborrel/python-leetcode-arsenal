# 2D Matrix Problems

These problems end up being an implicit graph problem using DFS or BFS. There will often be an extension to one of the 1d solutions you've come across.

You will have a `grid` that is represented by list of lists. Where each list represents a `row` and each element within it representing a `row` and `col` coordinate.

![Image](/problem_types/matrix/assets/2d%20grid.JPG)

## Solution Structure

Regardless of the problem type, you'll have this structure.

```python
# create the dimensions
rows = len(grid)
cols = len(grid[0])


# dfs
def dfs(r, c):

    # boundary check
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return False

    # answer check

    # exploration in directions
    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)


# traversing the grid
for r in range(rows):
    for c in range(cols):

        # check if grid coordinate meets criteria
        if grid[r][c] == criteria:
            # do something
```

## Creating a 2D Array

### Incorrect instantiation
- Creates a list containing multiple references to the same inner list
- If we change `arr[0][0] = 1`, then you'll end up with `[[1,0,0] , [1,0,0], [1,0,0]]`

```python
arr = [[0]* cols]* rows
```
### Correct instantiation
- This will create independent lists for each row
- Modifying one row doesn't affect the other ones.
- When using list comprehension, `[0] * cols` is run seperately for each, creating new lists with their own memory

```python
seen = [[0] * cols for _ in range(rows)]
```

## Example using Number of Islands

[Number of Islands](https://leetcode.com/problems/number-of-islands/)

![Image](/problem_types/matrix/assets/lc200-num-islands-dfs.jpg)


### Other Examples of questions

- [Battle Ships](https://leetcode.com/problems/battleships-in-a-board/description/)
- [Candy Crush](https://leetcode.com/problems/candy-crush/description/)
- [Crossword](https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/description/)