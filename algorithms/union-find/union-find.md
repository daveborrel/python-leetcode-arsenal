# Disjoint Set / Union Find

A Disjoint Set keeps track of a set fo elements partitioned into a number o disjoint sets (intersection of any two sets is null)

We can represent disjoint sets as trees

![Image](/algorithms/union-find/assets/disjoint%20sets.JPG)

There are two possible operations
- Union: Merging two sets into one.
- Find: Determines which subset a particular element belongs to.

### Setting up the parents array

In [LC684: Redundant Connection ](https://leetcode.com/problems/redundant-connection/description/)

- In this problem the nodes are labelled from 1 to n, and not 0 to n-1.
- If we used `range(n)` whenever we get a edge with node n we would need to subtract 1 to get its parent.
- By using `range(n+1)` we can have direct mapping of node labels to indices.

```
# If n = 3, nodes are labeled 1, 2, 3
self.parent = list(range(4))  # [0, 1, 2, 3]
# Index 0 is unused
# Node 1 uses index 1
# Node 2 uses index 2
# Node 3 uses index 3
```

```
N = len(edges)
parents = [i for i in range(N + 1)]
rank = [1] * (N + 1)
```

In [LC200: Number of Islands](https://leetcode.com/problems/number-of-islands/description/)

- We can use `range(n)` because its easier to map each grid cell to an index from 0 to (m*n)-1

```
Grid coordinates:       Mapped to linear indices:
(0,0) (0,1) (0,2) (0,3)    0     1     2     3
(1,0) (1,1) (1,2) (1,3) -> 4     5     6     7
(2,0) (2,1) (2,2) (2,3)    8     9    10    11
```


```
def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.rank = [1] * n
```


### Path Compression

Find function without path compression

```
def find(v):
    if v != parent[v]:
        return find(parent[v])
    return v
```

Find function with path compression

```
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

```
def union(v1, v2):
    parent[find(v2)] = find(v1)
```

```
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