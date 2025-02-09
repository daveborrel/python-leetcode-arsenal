class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        N = len(edges)

        #still struggling with list comprehension
        # this will give me [0, 1, 2, 3 ,4] = each node will be its own parent.
        parent = [i for i in range(N + 1)]

        def find(v):
            if v != parent[v]:
                return find(parent[v])
            return v

        def union(v1, v2):
            parent[find(v2)] = find(v1)
        
        for v1, v2 in edges:
            
            if find(v1) == find(v2):
                return [v1, v2]
            
            union(v1, v2)
            
s = Solution()
edges = [[1,2],[1,3],[2,3]]
ans = s.findRedundantConnection(edges=edges)
print(ans)