### List Comprehension

```python
# List comprehension
adj_list = [[] for _ in range(N)]

# Equivalent way to write this down
adj_list = []
for i in range(N):
    adj_list.append([])
```

### Sorted Function on Lists

- Returns the list in ascending order

[More detail here](https://docs.python.org/3/library/functions.html#sorted)

```python
a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
```

### Sorted Function on Dictionaries

The `sorted()` function will take in a second parameter called key, which is a function you can pass in to make comparisons with each element.

For example, if you use - `lambda x: (-x[1], x[0])`

For each element x, we'll sort them based on comparing the following:

- `-x[1]` The count, we add a negative sign in order to reverse the default order
- `x[0]` The letter value itself

```python
data = {
    "a": 3,
    "b": 3,
    "f": 9
}

# Sort by values (descending) and then by keys (ascending)
sorted_items = sorted(data.items(), key=lambda x: (-x[1], x[0]))

# Convert back to dictionary if needed (Python 3.7+ preserves insertion order)
sorted_dict = dict(sorted_items)

print(sorted_items)  # List of tuples: [('f', 9), ('a', 3), ('b', 3)]
print(sorted_dict)   # Dictionary: {'f': 9, 'a': 3, 'b': 3}
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

import heapq

s = []

heapq.heapify(x)
# transforms x into a heap, in-place, in linear time.

heapq.heappush(heap, item)
# pushes into the heap

heapq.heappush(heap)
# pops off the heap
```

### Using get function in dictionaries avoids having to set up an if / else case to check if the key exists or not.

```python
freq = {}

freq[nums[i]] = freq.get(nums[i], 0) + 1
# get will look up the array nums[i] and see if it is in the array
# if it doesn't exist return 0
# in this case, it doesn't exist it returns 0, but you'll increment it by one since its the first time you've seen it.
```

Its possible to return the sum of the values in a dictionary

```python
t = "ABC"

count_map = {}

for char in t:
    count_map[char] = count_map.get(char, 0) + 1

print(count_map)

print(sum(list(count_map.values()))) # prints 3
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

```python
for i in range(n-1, -1, -1)
```

### Enumerate

- This function adds a counter to each item in a list or other iterable. Where each item returns with its number / index and original value at that index.

```python
nums = [-1, 0, 1, 2, -1, -4]

for i in enumerate(nums):
    print(i)

# this will print out
# (0, -1)
# (1, 0) etc
```

### Join() operation is not the same as + when concatenating letters or strings together

- This function adds a counter to each item in a list or other iterable. Where each item returns with its number / index and original value at that index.

```python
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

```python
# to instantiate a queue
q = collections.deque()

# removes the first element from the queue making it FIFO as opposed to pop(), removing the last element on the right, which is LIFO
q.popleft()
```

### float is_integer()

```python
1.5.is_integer()
# False

1.0.is_integer()
# True

```

### Splicing in Python

- to begin, indexing is the process of accessing an element in a sequence using its position in the sequence.
- Splicing, however, is the process of accessing a subsequence of a sequence by specifying a starting and ending index

```python
sentence = "The quick brown fox jumps over the lazy dog"
first_word = sentence[:3]
print(first_word) # output: "The"

# remember that the [:3] syntax means that we include everything from the start of the string up until 3 (excluding 3)
```

### Operator module

```python
import operator

s = ["+", 1]

op = {"+": operator.add, "-": operator.sub , "*": operator.mul, "/": operator.floordiv}

val = op[s[0]] (s[1], 2)

print(val)
```

### Difference between int(a,b) and a//b

```python
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

```python
print(-9/5)
# returns -1.8

print(int(-9 / 5))
# returns -1 - closer to 0

print(-9 // 5)
# returns -2 - makes it smaller

```

### Lambda Functions

[more detail here](/python-tools/lamdba-functions.md)

```python
lambda x: x + 1
```

### Zip

- Takes two iterables (lists in most cases) and returns them in a single tuple.

[more detail here](https://www.programiz.com/python-programming/methods/built-in/zip)

```python
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

res = list(zip(position, speed))

print(res)

# prints out
# [(10, 2), (8, 4), (0, 1), (5, 1), (3, 3)]
```

### Set intersection

```python
intersect = len(elems[i] & elems[j])
```

### Getting STDIN

- Each call to input will take a line from the STDIN
- Using print() is essentially printing to STDOUT by default as well

```python
text = input()
```

### Python Reading and Writing to Files

**Reading a file**

```python
#open the file
text_file = open('/Users/pankaj/abc.txt','r')

#get the list of line
line_list = text_file.readlines()
```

**Writing to a file**

```python
# Appends to the file you opened
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# Overwrites the all the content
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
```

### Parsing Email with Regex

```python
def is_valid_email(email_address):
    # Regular expression pattern for email validation with the specific criteria:
    # - Username starts with an English letter and can contain alphanumeric chars, -, ., _
    # - Domain contains only English letters
    # - Extension contains only English letters and is 1-3 characters long
    pattern = r'^[a-zA-Z][\w\-\.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    return bool(re.match(pattern, email_address))
```

### Each component of the regex statement

- `^` is the start of the string
- `[a-zA-Z][\w\-\.]*` - checks if the start of the string begins with an alphanumeric, and then everythign afterwards can be alphanumeric as well including `-`, `.`, `_`
- `@` - Just the at sign
- `[a-zA-Z]` ensures domain is english letters
- `\.` literal period
- `[a-zA-Z]{1,3}` - The extension has english letters and is 1-3 letters long
- `$` end of the string

### Using exponents in python

If you want to use exponents, you must use a double star in order to calculate those values.

```
if -(2**31) <= val <= 2**31 - 1:
    return val
```

### **lt** magic method

This **lt**() method determines whether or not one object is less than another. Useful for when objects are closely related.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        if isinstance(other, Point):
             return (other.x, other.y) < (self.x, self.y)
        raise TypeError("Both objects should be instances of Point")

p1 = Point(3, 4)
p2 = Point(1, 2)
p3 = Point(3, 2)

print(p1 < p2)
print(p1 < p3)
print(p2 < p3)

#Raises an Error
print(p1 < (1, 2))
```
