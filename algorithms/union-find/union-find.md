# Disjoint Set / Union Find

A Disjoint Set keeps track of a set fo elements partitioned into a number o disjoint sets (intersection of any two sets is null).

We can represent disjoint sets as trees.

![Image](/algorithms/union-find/assets/disjoint%20sets.JPG)

In the leftmost case, where each disjoint set contains 1 element, each disjoint set's representative is itself.

![image](/algorithms/union-find/assets/union_find_parents_1.png)

![image](/algorithms/union-find/assets/union_find_parents_2.png)

## Setting up Parents Array

We often use a parents array to represent the parents of each disjoint set.

### Different Ways to Instantiate Parents Array

In [LC684: Redundant Connection ](https://leetcode.com/problems/redundant-connection/description/)

We have these graph nodes.

![image](/algorithms/union-find/assets/redundant%20connection.jpg)

We can use a single parents array to represent the parents of each node. The issue here is that the nodes are labelled from `1 to n`, instead of `0 to n-1`. Meaning, we would need to make a parents array 1 element larger than the range of nodes in order to let its index in the parents array match up with its actual node value.

- If we used `range(n)` whenever we get a edge with node n we would need to subtract 1 to get its parent.
- By using `range(n+1)` we can have direct mapping of node labels to indices.

```python
N = 4
self.parent = list(range(N))  # [0, 1, 2, 3]
# Index 0 is unused
# Node 1 uses index 0
# Node 2 uses index 1
# Node 3 uses index 2
# Node 4 uses index 3 --> This would be annoying as we need to account for that -1 different in each.

self.parent = list(range(N + 1))  # [0, 1, 2, 3, 4]
# Index 0 is unused
# Node 1 uses index 1
# Node 2 uses index 2
# Node 3 uses index 3
# Node 4 uses index 4 --> With this adjusted approach we can use the node to index itself.
```

```python
N = len(edges)
parents = [i for i in range(N + 1)]
rank = [1] * (N + 1)
```

In [LC200: Number of Islands](https://leetcode.com/problems/number-of-islands/description/)

In this problem, we need to figure out a way to map the 2D grid into a 1D parents array.

We can use this formula `r * cols + c` to do that conversion.
- `r * cols` - Slides the "window" over to correct row
- `+ c` - within that correct, "window"

![image](/algorithms/union-find/assets/2dgrid_into_1dparent_array.jpg)

- We can use `range(n)` because its easier to map each grid cell to an index from 0 to (m*n)-1

```
Grid coordinates:   Mapped to linear indices:
(0,0) (0,1) (0,2)    0     1     2     
(1,0) (1,1) (1,2) -> 3     4     5     
(2,0) (2,1) (2,2)    6     7     8    
```

Which results in this type of constructor
- Where we instantiate `parent` and `rank` array as empty arrays at first.

```python
    def __init__(self, grid):
        self.count = 0
        m, n = len(grid), len(grid[0])
        self.parent = []
        self.rank = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent.append(i * n + j)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)
```

Lets say we have this map of islands,

```
[[1,1,0],
 [1,0,0],  
 [0,0,1]]
```

After instantiating the array using the code from above, our parents array should look like:

```
[0,1,-1,3,-1,-1,-1,-1,8]
```

## Union Find Operations

There are two possible operations when working with these disjoint sets.

### Find: Determines which subset a particular element belongs to.

```
int find_set(int v) {
    if (v != parent[v])
        return v
    return find(parent[v])
}
```

### Union: Merging two sets into one.

```
void union(int a, int b) {
    parent_a = find(a)
    parent_b = find(b)
    if (a != b)
        parent[b] = a
}
```


### Path Compression

Find function without path compression

```python
def find(v):
    if v != parent[v]:
        return find(parent[v])
    return v
```

Find function with path compression

```python
def find_with_path_compression(v):
    if v != parent(v):
        return parent[v] = find_with_path_compression(parent[v])
    return v
```

- remember that `return parent[v] = find_with_path_compression(parent[v])` is a compound statement. Meaning that we actuall do these two steps:
    - assign return value of 1 to 3
    - return 1

![Image](/algorithms/union-find/assets/path_compression_1.JPG)
![Image](/algorithms/union-find/assets/path_compression_2.JPG)

### Union By Rank

- Here we are deciding which tree gets attached to which depending on the size of the tree.

```python
def union(v1, v2):
    parent[find(v2)] = find(v1)
```

```python
def union(v1, v2):
    p1, p2 = find(v1), find(v2)
    
    if p1 == p2:
        return False
    
    if rank[p1] > rank[p2]:
        parent[p2] = p1
        rank[p1] += rank[p2]
    else:
        parent[p1] = [p2]
        rank[p2] = rank[p1]
    return True
```