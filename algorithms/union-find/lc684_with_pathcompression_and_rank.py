class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        N = len(edges)

        #still struggling with list comprehension
        # this will give me [0, 1, 2, 3 ,4] = each node will be its own parent.
        parent = [i for i in range(N + 1)]
        rank = [1] * (N + 1)


        def find(v):
            if v != parent[v]:
                parent[v] = find(parent[v])
            return parent[v] # they will all end up having the same parent after all of this.

        def union(v1, v2):
            p1, p2 = find(v1), find(v2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for v1, v2 in edges:
            if not union(v1, v2):
                return [v1, v2]
            
s = Solution()
edges = [[1,2],[1,3],[2,3]]
ans = s.findRedundantConnection(edges=edges)
print(ans)