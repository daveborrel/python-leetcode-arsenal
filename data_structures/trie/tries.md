# Tries

a trie is a tree-like data structure where in the nodes of the tree store the entire alphabet and strings/words can be retrived by traversing down branch path of the tree.

#### Common Uses

- Autocomplete
- Spell Checker
- IP Routing

## Trie Node Structure

- Up to R links to its children. R depends on the language used. For most cases assumes R = 26 with lowercase latin letters.
- A boolean saying if the node is the end of a key or just a prefix.

Example of how it works. Taken from [this Medium article](https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014)

![img](/data_structures/trie/trie.JPG)
