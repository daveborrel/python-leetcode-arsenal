# BFS

- This is a way to traverse a graph or tree where it uses a queue to traverse the nodes of the the tree.

![image](/algorithms/bfs/static/bfs-traversal.jpg)

### Pseudocode

```
BFS (G, s)                   //Where G is the graph and s is the source node
      let Q be queue.
      Q.enqueue( s ) //Inserting s in queue until all its neighbour vertices are marked.

      mark s as visited.
      while ( Q is not empty)
           //Removing that vertex from queue,whose neighbour will be visited now
           v  =  Q.dequeue( )

          //processing all the neighbours of v
          for all neighbours w of v in Graph G
               if w is not visited
                        Q.enqueue( w )             //Stores w in Q to further visit its neighbour
                        mark w as visited.
```

## Common Problems that use BFS

### Shortest Path Between Two Points

- Getting the shortest path between two nodes is almost exclusively done using BFS, and all programmers should use this.

Useful Psuedocode for any BFS problem that includes a `nxn` grid.
The tricky thing to remember with a BFS problem is that we can just put the pair itself into the grid.

```python
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

define function get_neighbors(row, col):
neighbors = a container to put the neighbors of (row, col) in
    for each (row_direction, col_direction) pair in directions:
        neighbor_row = row + row_direction
        neighbor_col = col + col_direction
        if (neighbor_row, neighbor_col) is NOT over the edge of the grid AND is 0:
            add (neighbor_row, neighbor_col) to neighbors
    return neighbors
```

### Common BFS Patterns in Questions

- To ensure that all of the nodes in a specific level are checked, find the length of that level you're looking at.

Example from this leetcode question

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque([root])

        # when doing questions that iterate through all the levels
        while q:
            level_length = len(q)

            for i in range(level_length):
                node = q.popleft()

                if i == level_length - 1:
                    res.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res
```
