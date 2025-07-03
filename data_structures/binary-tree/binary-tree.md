# Binary Trees

### There are a few ways to traverse a binary tree

Inorder - Going from left subtree --> root --> right subtree
Preorder - Going from root --> left subtree --> right subtree
Postorder - left subtree --> right subtree --> root

Python Implementations

Inorder

```python
    def inorder(self,root):
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.data)
            res = res + self.inorder(root.right)
        return res
```

Preorder

```python
def preorder(self, root):
    res = []
    if root:
        res.append(root.data)
        res = res + self.preorder(root.left)
        res = res + self.preorder(root.right)
    return res
```

Postorder

```python
def postorder(self,root):
        res = []
        if root:
            res = self.postorder(root.left)
            res = res + self.postorder(root.right)
            res.append(root.data)

        return res
```

## Sources

[Binary Tree Traversals](https://www.freecodecamp.org/news/binary-search-tree-traversal-inorder-preorder-post-order-for-bst/)
