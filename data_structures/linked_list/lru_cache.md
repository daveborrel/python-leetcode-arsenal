# LRU Cache Implementation using doubly linked list

We use a doubly linked list because we can delete any node in O(n), this would not be the case with a singly linked list.

### Dummy Nodes

![image](/data_structures/linked_list/assets/doubly%20linkedlist.JPG)

Its useful to use dummy nodes in this example because it covers a bunch of edge cases
- When the list is empty
- Adding and removing the first node
- Adding and removing the last node
- Adding and removing the only node

### Absraction of Add and Remove

This makes it easier to understand what the rest of the code is doing.

### Add

![image](/data_structures/linked_list/assets/lru_add.JPG)

### Remove

![image](/data_structures/linked_list/assets/lru_remove.JPG)


```python
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)

        node = ListNode(key, value)
        self.dic[key] = node
        self.add(node)

        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]

    def add(self, node):
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```