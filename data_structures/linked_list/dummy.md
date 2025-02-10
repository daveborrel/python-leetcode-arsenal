### Dummy Nodes Explained

Dummmy Nodes - are useful to handle edges cases when dealing with linked list problems.

- These nodes will always point to the head of the linked list - even if you end up removing the head of the linked list.
- Help avoid special logic if we are building a single new linked list from two seperate ones.
- If we are filtering through a list and potentially remove the head of the list, its better to keep a dummy node to not lose context of the head.


### Related LeetCode Problems
- [LeetCode 19 - Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
    - We need this to point to the head of the linked list because there could be a good chance of removing the head node and we don't want to lose any context.
- [LeetCode 21 - Merge Two Sorted Lists](https://website-name.com)
    - We need the dummy node so that we don't have to use special logic to establish what the head will be.