# All Algorithms in a Single Place

# Binary Search Tree

Searching a Tree

```python
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return None

        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
```

DFS Tree Pattern

```python
def dfs(node, current_state):
    if not node:
        return base_case

    # Optional: if leaf node, check or return result
    if not node.left and not node.right:
        return check_something()

    left = dfs(node.left, updated_state)
    right = dfs(node.right, updated_state)

    return combine(left, right)
```
