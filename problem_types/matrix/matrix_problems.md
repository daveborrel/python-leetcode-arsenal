# Matrix Problems

These problems end up being an implicit graph problem using DFS or BFS. There will often be an extension to one of the 1d solutiosn you've come across.

## Creating a 2D Array

- Creates a list containing multiple references to the same inner list
- If we change `arr[0][0] = 1`, then you'll end up with `[[1,0,0] , [1,0,0], [1,0,0]]`

```python
arr = [[0]* cols]* rows
```

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

[Battle Ships](https://leetcode.com/problems/battleships-in-a-board/description/)
[Candy Crush](https://leetcode.com/problems/candy-crush/description/)
[Crossword](https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/description/)