# Redundant Connection

- There are two ways to solve this. Either by making a graph from the vertices that they provide or using a disjoint set.

### DFS

```
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # build the proper data structures
        N = len(edges)

        # creates a list of lists that is of length N
        # "for _" is just a convention to say that you want to iterate over something but don't want to use the value
        # in short, do this N times. Or make a list of lists that is N long.
        adj_list = [[] for _ in range(N)]

        for edge in edges:

            #created a visited data structure
            visited = [False] * N

            #check if the current edge creates a cycle
            if self._is_connected(edge[0] - 1, edge[1] - 1, visited, adj_list):
                return edge
            
            # add the edge to the graph
            adj_list[edge[0] - 1].append(edge[1] - 1) # add first vertex's neighbor
            adj_list[edge[1] - 1].append(edge[0] - 1) # add second vertex's neighbor

        return []

    def _is_connected(self, src, target, visited, adj_list):
        visited[src] = True

        # if recursively, we end up with src as the target, it means that the target is 
        # already connected to another
        # node, meaning there is another path to get there. This means that adding this 
        # edge would be adding a cycle. if that is the case, we can return this one node.
        if src == target:
            return True

        is_found = False

        # loop through the current node's neighbors
        for adj in adj_list[src]:

            # if the current neighbor isn't visited, then check if its connected.
            if not visited[adj]:
                is_found = is_found or self._is_connected(adj, target, visited, adj_list)
        
        return is_found
```

### Union Find

![image](/data_structures/graphs/asset/684-ep74-2.png)


Disjoint Set with Path Compression and Union By Rank

```
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parents = [i for i in range(N + 1)]
        rank = [1] * (N + 1)
        
        def find(n):
            if n != parents[n]:
                #instead of just returning this value, the parent of the current node will be the return value of the find() call.

                #this changes the tree structure.
                # so if we had 1 -> 2 -> 3 -> 4
                # it would be 1 -> 4, 2-> 4, 3-> 4 - where they all point to 4 but are still part of the same tree

                return parents[n] = find(parents[n]) 
            return parents[n]
        
        def union(n1, n2):
            # check if they are in the same tree - if they are return false
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            # check the size of each connected component - attach the smaller one to the larger one
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]
            return True
            
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
```

Disjoint set without path compression or union by rank

```
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)

        #setting up the parents array
        parents = [i for i in range(N + 1)]

        def find(n):
            if n != parents[n]:
                return find(parents[n])
            return n
        
        def union(n1, n2):
            parents[find(n2)] = find(n1)
        
        for n1, n2 in edges:

            #check if the parents are the same as the existing component.
            if find(n1) == find(n2):
                return [n1, n2]

            union(n1, n2)
```