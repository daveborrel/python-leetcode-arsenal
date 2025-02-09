# Need to instantiate a parents array
parent = {}

# makes a set
def make_set(v):
    parent[v] = v
    
def find(v):
    if v != parent[v]:
        return find(parent[v])
    return v

def union(v1, v2):
    parent[find(v2)] = find(v1)
        
make_set(1)
make_set(2)

union(1, 2)

print(f"{parent[1]} and {parent[2]}")