# Lambda Functions

- Python lambdas are annonymous functions that have more concisde notation.
- "Anonymous" in this context, simply means that this function does not have a name.

Standard function definition
```python
>>> def identity(x):
...     return x
```

Defining and using a lambda function
```python
lambda x: x + 1

# 2 will be the argument and this will print out 3
(lambda x: x + 1)(2)

# This expression can be named
add_one = lambda x: x + 1
add_one(2)
```