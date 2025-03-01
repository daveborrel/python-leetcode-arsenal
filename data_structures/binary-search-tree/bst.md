# Binary Search Tree

Binary Search Tree allows us to quickly maintain a sorted list of numbers.
We can search for the presence of a number in O(log(n)) time.

These properties seperate it from a regular binary tree.
- All nodes in the left subtree are less than the root node.
- All nodes in the right subtree are less than the root node.

### Tree Traversal Examples

[LC226: Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

- In this example, you reverse it in place at the current root level
- Then you use recursion to rotate its children.

![image](/data_structures/trees/assets/bst.JPG)


```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return root

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```

