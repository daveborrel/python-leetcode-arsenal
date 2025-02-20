### List Comprehension

```python
# List comprehension
adj_list = [[] for _ in range(N)]

# Equivalent way to write this down
adj_list = []
for i in range(N):
    adj_list.append([])
```

### Sorted

```python
a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
```

### Counter

```python
from collections import Counter   #counts the letters but has high overhead
s = "cat"
t = "act"

print(Counter(s))
print(Counter(t))

#Counter({'c': 1, 'a': 1, 't': 1})
#Counter({'a': 1, 'c': 1, 't': 1})
```

### Ord

```python
# returns the integer that represents the character "h"

print(ord('a'))
print(ord('a') - ord('a'))
print(ord('a') - ord('a'))

# 97
# 0 
# 19
```

### Removing Non Alphanumeric and Uppercase

```python
s = "A man, a plan, a canal: Panama"

s_removed = ''.join(filter(str.isalnum, s)) 
# ''.join() puts the filtered characters back together // 
# filter(str.isalnum, s) keeps only alphanumeric characters from s //
# str.isalnum is a builtin method of str, so it can be used directly //

print(s_removed) #AmanaplanacanalPanama
s_lower = s_removed.lower()
print(s_lower) #amanaplanacanalpanama
```

### Getting the floor of an integer value / Division

```python
res = (5 / 2)
print(res) 
# prints out 2.5 - which can result in floating number results

res1 = (5 // 2)
print(res1)
# prints out 2 - which can only be integer division.
```

### Tuples can be used to index into a hashmap in python

- We can’t use a list because it is mutable and can change.
- Also, anything in the tuple must not be mutable either.

```python
my_map = {
    (1, 2): "point A",
    ("x", "y", "z"): "coordinates"
}

print(my_map[(1, 2)])  # Output: point A

my_map = {
    ([1, 2], 3): "invalid key"  # ❌ This will raise a TypeError
}

```

### Heaps in Python

- by default is a minHeap https://docs.python.org/3/library/heapq.html
- to create a maxHeap - you can just push into the heap by multiplying each value by -1 and then multiplying it by -1 again once you need the values.

```python
s = []

heapq.heapify(x)
# transforms x into a heap, in-place, in linear time.

heapq.heappush(heap, item)
# pushes into the heap

heapq.heappush(heap)
# pops off the heap
```

### Using get to increment the counter faster in Python

```python
freq = {}

freq = freq.get(nums[i], 0) + 1
# get will look up the array nums[i] and see if it is in the array
# if it doesn't exist return 0
# in this case, it doesn't exist it returns 0, but you'll increment it by one since its the first time you've seen it.
```

### Creating a set

```python
seen = set()

# how to add and remove from the arrays
seen.add()
seen.remove()
```

### Slow and fast pointers to find middle of the list, and linked list cycles

```python
# creating this will give us two pointers, one fast, one slow.
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

### Stack in Python

- A list can be used as a stack

```python
s = [73,74,75,71,69,72,76,73]
s.pop()
print(s) #s = [73,74,75,71,69,72,76,73] - removes the end of the list
```

### Shallow vs Deep Copy

- If instead we did `temp = s`, they will point to the same place and we won’t have two seperate stacks here.

```python
s = [73,74,75,71,69,72,76,73]
s.pop()
temp = s.copy()

temp.pop()
temp.pop()
temp.pop()
temp.pop()

print(temp) #[73, 74, 75]
print(s)    #[73, 74, 75, 71, 69, 72, 76]
```

### Going through a list in reverse order - using reversed()

```python
>>> a = ["foo", "bar", "baz"]
>>> for i in reversed(a):
...     print(i)
... 
baz
bar
foo
```

### Going through a list in reverse order using range() function

- range takes in three possible arguments
    - start - where to start (inclusive)
    - stop - where to end (exclusive)
    - step - how much to increment/ decrement by

```
for i in range(n-1, -1, -1)
```

### Enumerate

- This function adds a counter to each item in a list or other iterable. Where each item returns with its number / index and original value at that index.

```
nums = [-1, 0, 1, 2, -1, -4]

for i in enumerate(nums):
    print(i)

# this will print out
# (0, -1)
# (1, 0) etc
```

### Join() operation is not the same as + when concatenating letters or strings together

- This function adds a counter to each item in a list or other iterable. Where each item returns with its number / index and original value at that index.

```
s = ["Hello","World"]
res = " "
print(res.join(s[0]))

# this will actually just print out H e l l o - because you're adding the " " between the letters you give it.
# In the more extreme example

print("acbdefg".join)

# this will just print out "Habcdefgeabcdefgl..." - where there is a abcdefg in between each portion.

```

### queues
- deque stands for double-ended queue. 


```
# to instantiate a queue
q = collections.deque()

# removes the first element from the queue making it FIFO as opposed to pop(), removing the last element on the right, which is LIFO
q.popleft()
```

### float is_integer()

```
1.5.is_integer()
# False

1.0.is_integer()
# True

```

### Splicing in Python
- to begin, indexing is the process of accessing an element in a sequence using its position in the sequence.
- Splicing, however, is the process of accessing a subsequence of a sequence by specifying a starting and ending index

```
sentence = "The quick brown fox jumps over the lazy dog"
first_word = sentence[:3]
print(first_word) # output: "The"

# remember that the [:3] syntax means that we include everything from the start of the string up until 3 (excluding 3)
```

### Operator module

```
import operator

s = ["+", 1]

op = {"+": operator.add, "-": operator.sub , "*": operator.mul, "/": operator.floordiv}

val = op[s[0]] (s[1], 2)

print(val)
```

### Difference between int(a,b) and a//b

```
a = 5
b = 2

# float division - 2.5
print(a/b)

# floor division - 2
print(a//b)

# truncation towards 0 - which means to chop off the decimal portion of a number.
print(int(a/b))
```

Using a more specific example for [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)

However, we run into a special case when looking at negative numbers:

-9 / 5 = ? (-1.8)

Most programming languages will will either do one of the following
- make it smaller by rounding to -2.
- make it closer to 0.

This is where int will do the trick

```
print(-9/5)
# returns -1.8

print(int(-9 / 5))
# returns -1 - closer to 0

print(-9 // 5)
# returns -2 - makes it smaller

```

