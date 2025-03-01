# Binary Tree


### Example fo Questions

[LC104: Maximum Depth of a Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

- In this question, you use recursion to add 1 to the count each time you traverse down a child subtree.
- Make sure that there is a base case that you return from depending on the result that you want.


```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
```


[LC543: Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

- Tricky easy question
- Need a global variable and using dfs to check the possibe depth




```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return self.res
```