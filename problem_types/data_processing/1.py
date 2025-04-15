# given s = "a?rt???"
# turn this into the smallest palindrome possibe

res = []
arr = [1,2,2,3,4]
low = [0,2]
high = [2,4]

ranges = []

for i in range(len(low)):
    curr_range = []
    
    curr_range.append(low[i])
    curr_range.append(high[i])
    ranges.append(curr_range)

count = 0

for i in range(len(ranges)):
    count = 0
    
    for val in arr:
        if ranges[i][0] <= val <= ranges[i][1]:
            count += 1
    
    res.append(count)
    
print(res)