# DFS

- This is a way to traverse a tree or a graph where we use backtracking as the primary method for traversal.

### pseudocode

```
    DFS-iterative (G, s):                                   //Where G is graph and s is source vertex
      let S be stack
      S.push( s )            //Inserting s in stack 
      mark s as visited.
      while ( S is not empty):
          //Pop a vertex from stack to visit next
          v  =  S.top( )
         S.pop( )
         //Push all the neighbours of v in stack that are not visited   
        for all neighbours w of v in Graph G:
            if w is not visited :
                     S.push( w )         
                    mark w as visited


    DFS-recursive(G, s):
        mark s as visited
        for all neighbours w of s in Graph G:
            if w is not visited:
                DFS-recursive(G, w)
```

### Different types of traversal on the binary search tree

[images taken from freeCodeCamp](https://www.freecodecamp.org/news/binary-search-tree-traversal-inorder-preorder-post-order-for-bst/)

- In all examples, we go as deep as we can go before backtracking. The only reason we have differences in the output is the order that we return to out function call stack.

### In Order Traversal

- Left, Root, Right
![image](/algorithms/dfs/static/in-order.JPG)


### Pre Order Traversal

- Root, Left, Right

![image](/algorithms/dfs/static/in-order.JPG)

### Post Order Traversal

- Right, Left, Root

![image](/algorithms/dfs/static/in-order.JPG)