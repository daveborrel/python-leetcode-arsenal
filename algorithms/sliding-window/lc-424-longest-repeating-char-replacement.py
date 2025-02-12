import collections

# Sliding Window + Binary Search

s = "AABABBA"

# counted = collections.Counter(s)

# print(counted.most_common())

l = r = 0

while r < len(s):
    print(s[l:r])
    r += 1