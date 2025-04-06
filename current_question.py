# Just a random python file for any testing you might have
# Think of this as replit

nums = [5,1,1,1,2]


def is_ascending(li):
    for i in range(0, len(li)-1):
        if li[i]<li[i+1]:
            pass
        else:
            return False
    return True

def get_pairs(li):
    dic = {}
    
    for i in range(0, len(li) - 1):
        curr_sum = li[i] + li[i+1]
        if curr_sum not in dic:
            dic[curr_sum] = [i, i+1]
    
    min_value = min(dic)
    
    return dic[min_value]

def replace_with_sum(li, start, end):
    curr_sum = li[start] + li[end]
    li[start] = curr_sum
    li.pop(end)

print(nums)

print(is_ascending(nums))
pairs = get_pairs(nums)
start = pairs[0]
end = pairs[1]

replace_with_sum(nums, start, end)

print(nums)
