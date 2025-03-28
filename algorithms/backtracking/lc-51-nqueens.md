# N - Queens

Taken from [leetcode](https://leetcode.com/problems/n-queens/description/)

"The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively."

### Brute Force

We can't just generate every single board state with N queens in it because it would take much too long.

## Backtracking

Remember from our general structure,

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


### Key Parts of Solution

- To ensure that there is only 1 queen per row, we'll only add a queen 1 row at a time and use that as a parameter
- Similarly, we can use a set to keep track of the col
- For diagonals its trickier but we can make use of these properties and have a set for each
    - All diagonals will have the same (row - col) value
    - All anti-diagonals will have the same (row + col) value


### Code

```python
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # Making use of a helper function to get the
        # solutions in the correct output format
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board

        def backtrack(row, diagonals, anti_diagonals, cols, state):
            # Base case - N queens have been placed
            if row == n:
                ans.append(create_board(state))
                return

            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                # If the queen is not placeable
                if (
                    col in cols
                    or curr_diagonal in diagonals
                    or curr_anti_diagonal in anti_diagonals
                ):
                    continue

                # "Add" the queen to the board
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                state[row][col] = "Q"

                # Move on to the next row with the updated board state
                backtrack(row + 1, diagonals, anti_diagonals, cols, state)

                # "Remove" the queen from the board since we have already
                # explored all valid paths using the above function call
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
                state[row][col] = "."

        ans = []
        empty_board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return ans
```